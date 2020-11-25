import numpy as np
import re
from datetime import datetime
import pandas as pd

from src.util.constants import *

# Checks to see if input row is a date
def is_date(date_td):
    return any(month in date_td.text for month in
               ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])


# Finds the game box elements from a table of games
def find_game_elements(table):
    # See https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class for syntax here
    return table.find_all('tr', class_=re.compile('TrGame*'))

# Replace text 'half' with '.5
def replace_half_with_decimal(text):
    return text.replace('½','.5')

# Extracts line or odds from string Ex: '-3 -120'
def convert_line(text, odds = False):
    if text != '':
        text = text.replace('EV','+100')
        length = len(text)
        split_location = re.search('[+-][1-9]\d{2}$',text).start(0)

    else:
        return 'Not Found'
    
    if odds:
        return text[length - split_location:].strip()
    else:
        return text[:split_location].strip()

# Replace o/u prefix with '-'/'' to standardize across books    
def total_line(text):
    if 'o' in text:
        return text.replace('o','-')
    else:
        return text.replace('u','')

# Retrieves data frame for game
def retrieve_data_frame_for_game(game, book_name = False):
    
    if book_name == 'Falcon':
        home_series = dict()
        home_series['Month'], home_series['Day'] = convert_integer_date(game['gmdt'])
        home_series['Team_ID'] = game['hnum']
        home_series['Internal_ID'] = game['idgm']
        home_series['Team'] = game['htm']
        home_series['Spread'] = game['GameLines'][0]['hsprdt']
        home_series['Spread_Line'] = game['GameLines'][0]['hsprdoddst']
        home_series['Total'] = game['GameLines'][0]['ovt']
        home_series['Total_Line'] = game['GameLines'][0]['ovoddst']
        
        away_series = dict()
        away_series['Month'], away_series['Day'] = convert_integer_date(game['gmdt'])
        away_series['Team_ID'] = game['vnum']
        away_series['Internal_ID'] = game['idgm']
        away_series['Team'] = game['vtm']
        away_series['Spread'] = game['GameLines'][0]['vsprdt']
        away_series['Spread_Line'] = game['GameLines'][0]['vsprdoddst']
        away_series['Total'] = game['GameLines'][0]['unt']
        away_series['Total_Line'] = game['GameLines'][0]['unoddst']
        
        return pd.DataFrame([pd.Series(home_series), pd.Series(away_series)])
    
    app_list = [np.nan for x in range(NUM_COLS)]
    td_arr = game.find_all('td')
    date_td = td_arr[DATE_IDX]
    if is_date(date_td):
        app_list[0] = date_td.text.split(' ')[0]
        app_list[1] = date_td.text.split(' ')[1]
    
    app_list[2] = td_arr[TEAM_ID_IDX].text.strip()
    app_list[4] = td_arr[TEAM_IDX].text.strip()
    
    if book_name == 'Dog':
        app_list[5] = convert_line(replace_half_with_decimal(td_arr[SPREAD_IDX].text.strip()))
        app_list[6] = convert_line(td_arr[SPREAD_IDX].text.strip(), odds = True)
        app_list[7] = convert_line(replace_half_with_decimal(total_line(td_arr[TOTAL_IDX].text.strip())))
        app_list[8] = convert_line(td_arr[TOTAL_IDX].text.strip(), odds = True)
    
    else:
        
        spread_td_elem = td_arr[SPREAD_IDX]
        if spread_td_elem.input is not None:
            spread_input_value = spread_td_elem.input['value']
            app_list[3] = spread_input_value.split('_')[1]
            app_list[5] = spread_input_value.split('_')[2]
            app_list[6] = spread_input_value.split('_')[3]
        
        else:
            app_list[3] = "Not Found"
            app_list[5] = "Not Found"
            app_list[6] = "Not Found"
            print("Team: {} lacks spread value".format(app_list[4]))

        total_td_elem = td_arr[TOTAL_IDX]
        if total_td_elem.input is not None:
            total_input_value = total_td_elem.input['value']
            app_list[7] = total_input_value.split('_')[2]
            app_list[8] = total_input_value.split('_')[3]
        else:
            app_list[7] = "Not Found"
            app_list[8] = "Not Found"
            print("Team: {} lacks total value".format(app_list[4]))

    return app_list


# Fills nan month and day for away teams
def fill_dates(df, first_row = False):
    if first_row:
        df.iloc[::2][['Month','Day']] = df[['Month','Day']].shift(-1).iloc[::2]
    else:
        df.iloc[1::2][['Month','Day']] = df[['Month','Day']].shift(1).iloc[1::2]
    return df

# Month Dictionary
month_dict = {
    '01': 'Jan',
    '02': 'Feb',
    '03': 'Mar',
    '04': 'Apr',
    '05': 'May',
    '06': 'Jun',
    '07': 'Jul',
    '08': 'Aug',
    '09': 'Sep',
    '10': 'Oct',
    '11': 'Nov',
    '12': 'Dec'
    }

# Converts date from 'yyyymmdd' to month and day
def convert_integer_date(date, month_dict = month_dict):
    new_date = datetime.strptime(date.strip(), '%Y%m%d').strftime('%m/%d/%Y')
    first_slash = new_date.find('/')
    second_slash = new_date.find('/', first_slash + 1)
    return month_dict[new_date[:first_slash]], new_date[first_slash + 1: second_slash]
    