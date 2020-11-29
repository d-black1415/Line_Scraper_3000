import json

import requests

from src.credentials.cred_reader import CredentialReader
from src.sportsbooks.sportsbook import SportsBook
from src.util.sportsbook_constants.bookie_market_constants import *


class BookieMarket(SportsBook):
    def __init__(self):
        super().__init__()
        self.book_name = 'BookieMarket'


    def login_and_retrieve_nfl_page(self):
        with requests.Session() as s:
            bm_creds = CredentialReader.read_cred_row(BOOKIE_MARKET_ROW_IDX)
            BM_LOGIN_FORM['txtLogin'] = bm_creds[0]
            BM_LOGIN_FORM['txtPassword'] = bm_creds[1]

            s.post(BM_LOGIN_URL, data=BM_LOGIN_FORM)

            nfl_page = s.post(BM_NFL_URL, headers=BM_HEADERS, json=BM_DATA_JSON)
            print(nfl_page.text)

    def retrieve_nfl_data_frame(self):
        self.login_and_retrieve_nfl_page()
        pass