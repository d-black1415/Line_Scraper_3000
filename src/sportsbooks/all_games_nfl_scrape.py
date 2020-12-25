import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from src.util.helpers import convert_line, replace_half_with_decimal, total_line, retrieve_data_frame_for_game
from src.credentials.cred_reader import CredentialReader
from src.sportsbooks.sportsbook import SportsBook
from src.util.sportsbook_constants.all_games_constants import *

class AllGames(SportsBook):
    
    def __init__(self):
        super().__init__()
        self.book_name = 'All_Games'

    def login_and_retrieve_nfl_page(self):
        with requests.Session() as s:
            all_games_creds = CredentialReader.read_cred_row(ALL_GAMES_CRED_ROW_IDX)
            ALL_GAMES_LOGIN_FORM = dict()
            ALL_GAMES_LOGIN_FORM['UserName'] = all_games_creds[0]
            ALL_GAMES_LOGIN_FORM['Password'] = all_games_creds[1]
            login_req = s.post(ALL_GAMES_LOGIN_URL, data = ALL_GAMES_LOGIN_FORM)
            cookies = login_req.cookies
            return s.post(ALL_GAMES_NFL_URL, headers=NFL_HEADERS, data=NFL_FORM_DATA, cookies = cookies)
        
    def retrieve_nfl_data_frame(self):
        self.nfl_games_frame['MoneyLine'] = ''
        nfl_page = self.login_and_retrieve_nfl_page()
        nfl_page_parsed = BeautifulSoup(nfl_page.text, 'html.parser')
        games = nfl_page_parsed.find_all('div',{'id': re.compile(REGEX_GAME_FINDER)})
        for game in games:
            game_frame = retrieve_data_frame_for_game(game, self.book_name)
            self.nfl_games_frame = self.nfl_games_frame.append(game_frame, ignore_index = True)
