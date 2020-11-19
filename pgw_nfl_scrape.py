import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import sys
import pdb

from util.PGW_constants import *

def main():
    with requests.Session() as s:
        accountData = {}
        accountData[ACCOUNT] = sys.argv[1]
        accountData[PASSWORD] = sys.argv[2]
        accountData.update(PGW_LOGIN_FORM)
        
        login_resp = s.post(PGW_LOGIN_URL, data = accountData)
        cookies = login_resp.cookies
        nfl_page = s.post(PGW_SPORTS_URL, headers = NFL_HEADERS, params = REQ_PARAMS, data = NFL_FORM_DATA, cookies = cookies)
    
    parsed_nfl_page = BeautifulSoup(nfl_page.text, 'html.parser')
    # See https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class for syntax here
    nfl_box = parsed_nfl_page.find_all('tr', class_ = re.compile('TrGame*'))
    
    games = pd.DataFrame(columns=['Month', 'Day', 'Game_ID', 'Internal_ID', 'Team', 'Spread',
                                     'Spread_Line', 'Total', 'Total_Line'])
    
    for game in nfl_box:
        app_list = retrieve_app_list_for_game(game)
        games = games.append(pd.Series(app_list, index=games.columns), ignore_index=True)
    
    
def retrieve_app_list_for_game(game):
    app_list = [np.nan for x in range(NUM_COLS)]
    td_arr = game.find_all('td')
    date_td = td_arr[DATE_IDX]
    if isDate(date_td):
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
    print(app_list)
    return app_list

# Checks to see if input row is a date
def isDate(date_td):
    return any(month in date_td.text for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

if __name__ == '__main__':
    main()