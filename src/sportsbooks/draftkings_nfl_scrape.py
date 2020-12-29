import requests
import pandas as pd
import json
from src.util.helpers import retrieve_data_frame_for_game
from src.credentials.cred_reader import CredentialReader
from src.sportsbooks.sportsbook import SportsBook
from src.util.sportsbook_constants.legal_books_constants import *

class DraftKings(SportsBook):

    def __init__(self):
        super().__init__()
        self.book_name = 'Draftkings'
    
    def login_and_retrieve_nfl_page(self):
        with requests.Session() as s:
            homepage = s.get(NFL_URL, headers=NFL_HEADERS, params=NFL_PARAMS)
        
        data = json.loads(homepage.text)
        return data['results']
    
    def retrieve_nfl_data_frame(self):
        nfl_data = self.login_and_retrieve_nfl_page()
        for game in nfl_data:
            game_frame = retrieve_data_frame_for_game(game, self.book_name)
            self.nfl_games_frame = self.nfl_games_frame.append(game_frame, ignore_index = True)
            