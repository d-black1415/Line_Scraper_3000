import pandas as pd
import requests
from bs4 import BeautifulSoup

from src.credentials.cred_reader import CredentialReader
from src.sportsbooks.sportsbook import SportsBook

from src.util.helpers import find_game_elements, retrieve_data_frame_for_game, fill_dates
from src.util.sportsbook_constants.bfa_constants import *


class BetFastAction(SportsBook):

    def __init__(self):
        super().__init__()
        self.book_name = "BetFastAction"

    def login_and_retrieve_nfl_page(self):
        with requests.Session() as s:
            bfa_creds = CredentialReader.read_cred_row(BFA_CRED_ROW_IDX)
            account_data = {ACCOUNT: bfa_creds[0], PASSWORD: bfa_creds[1]}

            login_resp = s.post(BFA_LOGIN_URL, data=account_data)
            cookies = login_resp.cookies
            return s.post(BFA_SPORTS_URL, headers=NFL_HEADERS, params=REQ_PARAMS, cookies=cookies, data=NFL_FORM_DATA)

    def retrieve_nfl_data_frame(self):
        nfl_page = self.login_and_retrieve_nfl_page()

        nfl_page_parsed = BeautifulSoup(nfl_page.text, 'html.parser')

        table = nfl_page_parsed.find('table')
        nfl_box = find_game_elements(table)

        for game in nfl_box:
            game_data_frame = retrieve_data_frame_for_game(game)
            self.nfl_games_frame = self.nfl_games_frame.append(
                pd.Series(game_data_frame, index=self.nfl_games_frame.columns), ignore_index=True)
        
        self.nfl_games_frame = fill_dates(self.nfl_games_frame)