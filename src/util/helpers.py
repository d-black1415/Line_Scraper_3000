import numpy as np
import re
from datetime import datetime
import pandas as pd
from src.util.constants import *
import pdb
# Checks to see if input row is a date
def is_date(date_td):
    return any(month in date_td.text for month in
               ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])


# Finds the game box elements from a table of games
def find_game_elements(table):
    # See https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class for syntax here
    return table.find_all('tr', class_=re.compile('TrGame*'))


# Replace text 'half' with '.5'
def replace_half_with_decimal(text):
    return text.replace('½', '.5').replace(' ','')

# Replace text 'Even' with '+100'
def bmarket_clean_line(line):
    return line.replace('Even','+100')

# Decimal odds to American Odds
def decimal_to_american(line):
    if line < 2:
        return int(round(-100/(line - 1),0))
    else:
        return int(round((line - 1)*100,0))
    
# Extracts line or odds from string Ex: '-3 -120'
def convert_line(text, odds=False):
    if text != '':
        text = text.replace('EV', '+100')
        length = len(text)
        split_location = re.search('[+-][1-9]\d{2}$', text).start(0)

    else:
        return 'Not Found'

    if odds:
        return text[split_location:].strip().replace(' ','')
    else:
        return replace_half_with_decimal(text[:split_location].strip())


# Replace o/u prefix with '-'/'' to standardize across books
def total_line(text):
    if 'Ov' in text:
        return text.replace('Ov','-').strip()
    elif 'Un' in text:
        return text.replace('Un','').strip()
    elif 'o' in text:
        return text.replace('o', '-')
    else:
        return text.replace('u', '')

# Clean play365 Team Names by removing time
def play365_team_name_clean(name):
    if any(letter.isdigit() for letter in name):
        cutoff = re.search('\d',name).start()
        return name[:cutoff].strip()
    else:
        return name.strip()

        

# Retrieves data frame for game
def retrieve_data_frame_for_game(game, book_name=False):
    
    if book_name in ['Bet_Rivers_IL', 'Draftkings', 'Fanduel', 'Pointsbet']:
        month = datetime.fromtimestamp(game['date']/1000).strftime('%m')
        day = datetime.fromtimestamp(game['date']/1000).strftime('%d')
    
        try:
            home_team_initials = game['team2Initials']
        except:
            home_team_initials = 'Not Found'
            
        try:
            home_team_name = game['team2Name']
        except:
            home_team_name = 'Not Found'
            
        home_team = " ".join([name_part for name_part in [home_team_initials,home_team_name] if name_part != 'Not Found'])
            
        try:
            away_team_initials = game['team1Initials']
        except:
            away_team_initials = 'Not Found'
            
        try:
            away_team_name = game['team1Name']
        except:
            away_team_name = 'Not Found'
            
        away_team = " ".join([name_part for name_part in [away_team_initials,away_team_name] if name_part != 'Not Found'])
            
    
        temp_data = game['odds']
    
        for x in temp_data:
            
            home_dict = dict()
            away_dict = dict()
            
            away_dict['Month'] = month
            home_dict['Month'] = month
            away_dict['Day'] = day
            home_dict['Day'] = day
            away_dict['Team'] = away_team
            home_dict['Team'] = home_team
            
            if x['provider'] == book_name.upper():
                
                try:
                    away_dict['MoneyLine'] = decimal_to_american(x['moneyLine1'])
                    home_dict['MoneyLine'] = decimal_to_american(x['moneyLine2'])
                    
                except:
                    away_dict['MoneyLine'] = 'Not Found'
                    home_dict['MoneyLine'] = 'Not Found'
                    
                try:
                    away_dict['Total'] = x['overUnder']
                    home_dict['Total'] = '-' + str(x['overUnder'])
                    away_dict['Total_Line'] = decimal_to_american(x['overUnderLineUnder'])
                    home_dict['Total_Line'] = decimal_to_american(x['overUnderLineOver'])
                
                except:
                    away_dict['Total'] = 'Not Found'
                    home_dict['Total'] = 'Not Found'
                    away_dict['Total_Line'] = 'Not Found'
                    home_dict['Total_Line'] = 'Not Found'
                    
                try:    
                    away_dict['Spread'] = x['spread']*-1
                    home_dict['Spread'] = x['spread']
                    away_dict['Spread_Line'] = decimal_to_american(x['spreadLine1'])
                    home_dict['Spread_Line'] = decimal_to_american(x['spreadLine2'])
                
                except:
                    away_dict['Spread'] = 'Not Found'
                    home_dict['Spread'] = 'Not Found'
                    away_dict['Spread_Line'] = 'Not Found'
                    home_dict['Spread_Line'] = 'Not Found'
                    
                away_series = pd.Series(away_dict)
                home_series = pd.Series(home_dict)
            
                return pd.DataFrame([away_series, home_series])
        
        away_dict['MoneyLine'] = 'Not Found'
        home_dict['MoneyLine'] = 'Not Found'
        away_dict['Total'] = 'Not Found'
        home_dict['Total'] = 'Not Found'
        away_dict['Total_Line'] = 'Not Found'
        home_dict['Total_Line'] = 'Not Found'
        away_dict['Spread'] = 'Not Found'
        home_dict['Spread'] = 'Not Found'
        away_dict['Spread_Line'] = 'Not Found'
        home_dict['Spread_Line'] = 'Not Found'
        
        away_series = pd.Series(away_dict)
        home_series = pd.Series(home_dict)
        
        return pd.DataFrame([away_series, home_series])
        
        
    if book_name == 'Play365':
        game_dict = dict()
        game_dict['Team_ID'] = game.find('div',{'class':re.compile('^linesRot')}).text
        
        try:
            game_dict['Team'] = play365_team_name_clean(game.find('div',{'class': re.compile('^linesTeam')}).text[3:])
        except:
            game_dict['Team'] = 'Not Found'
        
        try:
            game_dict['Spread'] = convert_line(game.find('div',{'class':re.compile('^linesSpread')}).a.text, odds = False)
            game_dict['Spread_Line'] = convert_line(game.find('div',{'class':re.compile('^linesSpread')}).a.text, odds = True)
        except:
            game_dict['Spread'] = 'Not Found'
            game_dict['Spread_Line'] = 'Not Found'
        
        try:
            game_dict['Total'] = total_line(convert_line(game.find('div',{'class':re.compile('^linesMl')}).a.text, odds = False))
            game_dict['Total_Line'] = convert_line(game.find('div',{'class':re.compile('^linesMl')}).a.text, odds = True)
        except:
            game_dict['Total'] = 'Not Found'
            game_dict['Total_Line'] = 'Not Found'

        try:
            game_dict['MoneyLine'] = game.find('div',{'class':re.compile('^linesTotal')}).a.text.replace('EV','+100')
        except:
            game_dict['MoneyLine'] = 'Not Found'
        
        return pd.Series(game_dict)
    
    if book_name == 'All_Games':
        away_dict = dict()
        rows = game.find_all('div',{'class': re.compile('^row')})
        away = rows[0]
        away_game_info = away.find_all('span',{'class': re.compile('^lbet-')})    
        away_dict['Team_ID'] = re.sub('[^0-9]', '', away_game_info[0].text)
        away_dict['Team'] = away_game_info[1].text
        away_lines = away.find_all('label',{'class':'custom-control-label'})
        if len(away_lines) > 0:
            away_dict['Spread'] = convert_line(away_lines[0].text)
            away_dict['Spread_Line'] = convert_line(away_lines[0].text, odds = True)
        if len(away_lines) > 1:
            away_dict['Total'] = total_line(convert_line(away_lines[1].text))
            away_dict['Total_Line'] = total_line(convert_line(away_lines[1].text, odds = True))   
            if len(away_lines) > 2:
                away_dict['MoneyLine'] = away_lines[2].text
        else:
            away_dict['Total'] = 'Not Found'
            away_dict['Total_Line'] = 'Not Found'
            away_dict['MoneyLine'] = 'Not Found'
            
        away_series = pd.Series(away_dict)
        
        
        home_dict = dict()
        home = rows[1]
        home_game_info = home.find_all('span',{'class': re.compile('^lbet-')})    
        home_dict['Team_ID'] = re.sub('[^0-9]', '', home_game_info[0].text)
        home_dict['Team'] = home_game_info[1].text
        home_lines = home.find_all('label',{'class':'custom-control-label'})
        if len(home_lines) > 0:
            home_dict['Spread'] = convert_line(home_lines[0].text)
            home_dict['Spread_Line'] = convert_line(home_lines[0].text, odds = True)
        if len(home_lines) > 1:
            home_dict['Total'] = total_line(convert_line(home_lines[1].text))
            home_dict['Total_Line'] = total_line(convert_line(home_lines[1].text, odds = True))
            if len(home_lines) > 2:
                home_dict['MoneyLine'] = home_lines[2].text
            else:
                home_dict['MoneyLine'] = 'Not Found'
        else:
            home_dict['Total'] = 'Not Found'
            home_dict['Total_Line'] = 'Not Found'
            home_dict['MoneyLine'] = 'Not Found'
    
        home_series = pd.Series(home_dict)
        
        return pd.DataFrame([home_series, away_series])
            
    if book_name == 'BookieMarket':
        if game.find('span',{'class': re.compile('team-name[0-9]')}).text[0] == '1':
            return pd.DataFrame()
        team_data = game.find_all('div',{'class':'some-space'})
        temp_frame = pd.DataFrame()
        for team in team_data[:2]:
            temp_dict = dict()
            temp_dict['Team'] = team.find('span',{'class': re.compile('team-name[0-9]')}).text
            temp_dict['Team_ID'] = team.find('span',{'class':'time'}).text
            temp_dict['Internal_ID'] = game['id'][12:-3]
            temp_dict['MoneyLine'] = bmarket_clean_line(replace_half_with_decimal(team.find('li',{'class':re.compile('^money')}).find('span',{'class':'money-limit'}).text))
            temp_dict['Spread'] = replace_half_with_decimal(team.find('li',{'class':re.compile('^spread')}).find('span',{'class':'upper-limit'}).text)
            temp_dict['Spread_Line'] = bmarket_clean_line(replace_half_with_decimal(team.find('li',{'class':re.compile('^spread')}).find('span',{'class':'lower-limit'}).text))
            temp_dict['Total'] = replace_half_with_decimal(''.join([item.text for item in team.find('li',{'class':re.compile('^total')}).find_all('span',{'class':'upper-limit'})]))
            temp_dict['Total_Line'] = bmarket_clean_line(replace_half_with_decimal(team.find('li',{'class':re.compile('^total')}).find('span',{'class':'lower-limit'}).text))
            temp_dict['Month'], temp_dict['Day'] = ['','']
            temp_frame = temp_frame.append(pd.Series(temp_dict), ignore_index = True)
        return temp_frame
    
    if book_name == 'Falcon':
        # pdb.set_trace()
        home_series = dict()
        home_series['Month'], home_series['Day'] = convert_integer_date(game['gmdt'])
        home_series['Team_ID'] = game['hnum']
        home_series['Internal_ID'] = game['idgm']
        home_series['Team'] = game['htm']
        home_series['Spread'] = game['GameLines'][0]['hsprdt']
        home_series['Spread_Line'] = game['GameLines'][0]['hsprdoddst']
        home_series['Total'] = game['GameLines'][0]['ovt']
        home_series['Total_Line'] = game['GameLines'][0]['ovoddst']
        home_series['MoneyLine'] = game['GameLines'][0]['hoddsh'] if len(game['GameLines'][0]['hoddsh']) > 1 else "Not Found"
        
        away_series = dict()
        away_series['Month'], away_series['Day'] = convert_integer_date(game['gmdt'])
        away_series['Team_ID'] = game['vnum']
        away_series['Internal_ID'] = game['idgm']
        away_series['Team'] = game['vtm']
        away_series['Spread'] = game['GameLines'][0]['vsprdt']
        away_series['Spread_Line'] = game['GameLines'][0]['vsprdoddst']
        away_series['Total'] = game['GameLines'][0]['unt']
        away_series['Total_Line'] = game['GameLines'][0]['unoddst']
        away_series['MoneyLine'] = game['GameLines'][0]['voddst'] if len(game['GameLines'][0]['voddst']) > 1 else "Not Found"

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
        app_list[5] = convert_line(replace_half_with_decimal(td_arr[SPREAD_IDX].text.strip())).replace('PK','0')
        app_list[6] = convert_line(td_arr[SPREAD_IDX].text.strip(), odds=True)
        app_list[7] = convert_line(replace_half_with_decimal(total_line(td_arr[TOTAL_IDX].text.strip())))
        app_list[8] = convert_line(td_arr[TOTAL_IDX].text.strip(), odds=True)
        app_list[9] = td_arr[ML_IDX].text.strip() if len(td_arr[ML_IDX].text.strip()) > 3 else 'Not Found'

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
        
        ml_td_elem = td_arr[ML_IDX]
        if ml_td_elem.input is not None:
            ml_td_elem_value = ml_td_elem.input['value']
            app_list[9] = int(ml_td_elem_value.split('_')[-1])
        else:
            app_list[9] = "Not Found"
            
    return app_list


# Fills nan month and day for away teams
def fill_dates(df):
    for idx, row in df.iterrows():
        if idx % 2 != 0:
            df.loc[idx, "Month"] = df.loc[idx - 1, "Month"]
            df.loc[idx, "Day"] = df.loc[idx - 1, "Day"]
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
def convert_integer_date(date):
    new_date = datetime.strptime(date.strip(), '%Y%m%d').strftime('%m/%d/%Y')
    new_date_parts = new_date.split('/')
    return month_dict[new_date_parts[0]], new_date_parts[1]
