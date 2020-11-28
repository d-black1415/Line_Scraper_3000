import pandas as pd
import requests

from src.credentials.cred_reader import CredentialReader
from src.sportsbooks.sportsbook import SportsBook
from src.util.helpers import retrieve_data_frame_for_game, convert_integer_date
from src.util.sportsbook_constants.falcon_constants import *

class Falcon(SportsBook):
    def __init__(self):
        super().__init__()
        self.book_name = 'Falcon'
        
    def login_and_retrieve_nfl_page(self):
        with requests.Session() as s:
            falcon_creds = CredentialReader.read_cred_row(FALCON_CRED_ROW_IDX)
            FALCON_LOGIN_FORM['account'] = falcon_creds[0]
            FALCON_LOGIN_FORM['password'] = falcon_creds[1]
            
            login_req = s.post(FALCON_LOGIN_URL, data = FALCON_LOGIN_FORM)
            
            nfl_page = s.get(FALCON_NFL_URL, headers = NFL_HEADERS, params = REQ_PARAMS)
            nfl_box = nfl_page.json()
            return nfl_box['result']['listLeagues'][0][0]['Games']

    def retrieve_nfl_data_frame(self):
        nfl_page = self.login_and_retrieve_nfl_page()
        for game in nfl_page:
            game_frame = retrieve_data_frame_for_game(game, self.book_name)
            self.nfl_games_frame = self.nfl_games_frame.append(game_frame, ignore_index = True)
