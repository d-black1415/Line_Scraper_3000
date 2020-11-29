import requests
from bs4 import BeautifulSoup
import pandas as pd

from src.credentials.cred_reader import CredentialReader
from src.sportsbooks.sportsbook import SportsBook
from src.util.helpers import retrieve_data_frame_for_game, find_game_elements, fill_dates
from src.util.sportsbook_constants.pgw_constants import *


class PGW(SportsBook):

    def __init__(self):
        super().__init__()
        self.book_name = "PGW"

    def login_and_retrieve_nfl_page(self):
        with requests.Session() as s:
            pgw_creds = CredentialReader.read_cred_row(PGW_CRED_ROW_IDX)
            PGW_LOGIN_FORM[ACCOUNT] = pgw_creds[0]
            PGW_LOGIN_FORM[PASSWORD] = pgw_creds[1]

            login_resp = s.post(PGW_LOGIN_URL, data=PGW_LOGIN_FORM)
            cookies = login_resp.cookies
            return s.post(PGW_SPORTS_URL, headers=NFL_HEADERS, params=REQ_PARAMS, data=NFL_FORM_DATA, cookies=cookies)

    def retrieve_nfl_data_frame(self):
        nfl_page = self.login_and_retrieve_nfl_page()
        parsed_nfl_page = BeautifulSoup(nfl_page.text, 'html.parser')
        nfl_box = find_game_elements(parsed_nfl_page)

        for game in nfl_box:
            game_data_frame = retrieve_data_frame_for_game(game)
            self.nfl_games_frame = self.nfl_games_frame.append(
                pd.Series(game_data_frame, index=self.nfl_games_frame.columns), ignore_index=True)

        self.nfl_games_frame = fill_dates(self.nfl_games_frame)