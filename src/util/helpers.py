import numpy as np
import re

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
def clean_line(text):
    return text.replace('½','.5')

# Extracts line or odds from string Ex: '-3 -120'
def convert_line(text, odds = False):
    length = len(text)
    if odds:
        return text[length - 4:].strip()
    else:
        return text[:length - 4].strip()

# Replace o/u prefix with '-'/'' to standardize across books    
def total_line(text):
    if 'o' in text:
        return text.replace('o','-')
    else:
        return text.replace('u','')

# Retrieves data frame for game
def retrieve_data_frame_for_game(game):
    app_list = [np.nan for x in range(NUM_COLS)]
    td_arr = game.find_all('td')
    date_td = td_arr[DATE_IDX]
    if is_date(date_td):
        app_list[0] = date_td.text.split(' ')[0]
        app_list[1] = date_td.text.split(' ')[1]
    app_list[2] = td_arr[TEAM_ID_IDX].text.strip()
    app_list[4] = td_arr[TEAM_IDX].text.strip()
    spread_input_value = td_arr[SPREAD_IDX].input['value']
    app_list[3] = spread_input_value.split('_')[1]
    app_list[5] = spread_input_value.split('_')[2]
    app_list[6] = spread_input_value.split('_')[3]
    total_input_value = td_arr[TOTAL_IDX].input['value']
    app_list[7] = total_input_value.split('_')[2]
    app_list[8] = total_input_value.split('_')[3]
    return app_list

# Retrieves data frame for game on Dog
def dog_retrieve_data_frame_for_game(game):
    app_list = [np.nan for x in range(NUM_COLS)]
    td_arr = game.find_all('td')
    date_td = td_arr[DATE_IDX]
    if is_date(date_td):
        app_list[0] = date_td.text.split(' ')[0]
        app_list[1] = date_td.text.split(' ')[1]
    app_list[2] = td_arr[TEAM_ID_IDX].text.strip()
    app_list[4] = td_arr[TEAM_IDX].text.strip() 
    app_list[5] = clean_line(convert_line(td_arr[SPREAD_IDX].text.strip()))
    app_list[6] = convert_line(td_arr[SPREAD_IDX].text.strip(), odds = True)
    app_list[7] = clean_line(total_line(convert_line(td_arr[TOTAL_IDX].text.strip())))
    app_list[8] = convert_line(td_arr[TOTAL_IDX].text.strip(), odds = True)
    return app_list

# Fills nan month and day for away teams
def fill_dates(df, first_row = False):
    if first_row:
        df.iloc[::2][['Month','Day']] = df[['Month','Day']].shift(-1).iloc[::2]
    else:
        df.iloc[1::2][['Month','Day']] = df[['Month','Day']].shift(1).iloc[1::2]
    return df

