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
