import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from src.util.helpers import convert_line, replace_half_with_decimal, total_line, retrieve_data_frame_for_game, play365_team_name_clean
from src.credentials.cred_reader import CredentialReader
from src.sportsbooks.sportsbook import SportsBook
from src.util.sportsbook_constants.play365_constants import *

class Play365(SportsBook):
    def __init__(self):
        super().__init__()
        self.book_name = 'Play365'

    def login_and_retrieve_nfl_page(self):    
        with requests.Session() as s:
            play365_creds = CredentialReader.read_cred_row(PLAY365_CREDS_ROW_IDX)
            PLAY365_LOGIN_FORM_DATA['account'] = play365_creds[0]
            PLAY365_LOGIN_FORM_DATA['password'] = play365_creds[1]
            login_req = s.post(PLAY365_LOGIN_URL, data = PLAY365_LOGIN_FORM_DATA)
            cookies = login_req.cookies
            NFL_DATA['pi'] = f'{play365_creds[0]}|{play365_creds[1]}'
            return s.post(PLAY365_NFL_URL, headers = NFL_HEADERS, data = NFL_DATA, cookies = cookies)
    
    def retrieve_nfl_data_frame(self):
        self.nfl_games_frame['MoneyLine'] = ''
        nfl_page = self.login_and_retrieve_nfl_page()
        nfl_parsed_page = BeautifulSoup(nfl_page.text, 'html.parser')
        games = nfl_parsed_page.find_all('div',{'class':re.compile(REGEX_GAME_FINDER)})
        for game in games:
            game_frame = retrieve_data_frame_for_game(game, self.book_name)
            self.nfl_games_frame = self.nfl_games_frame.append(game_frame, ignore_index = True)
    