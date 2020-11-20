import requests
from bs4 import BeautifulSoup
import pandas as pd

from src.sportsbooks.sportsbook import SportsBook

from src.util.constants import *
from src.util.sportsbook_constants.dog_constants import *
from src.util.helpers import *

class Dog(Sportsbook):
    
    def __init__(self):
        super().__init__()
        self.book_name = "Dog"
        
    def login_and_retrieve_nfl_page(self):
        return requests.post(DOG_BASE_URL, params=REQ_PARAMS)

    def retrieve_nfl_data_frame(self):
        nfl_page = self.login_and_retrieve_nfl_page()
        
        nfl_page_parsed = BeautifulSoup(nfl_page.text, 'html.parser')        
        
        nfl_box = find_game_elements(test)


        for game in nfl_box:
            game_data_frame = dog_retrieve_data_frame_for_game(game)
            self.nfl_games_frame = self.nfl_games_frame.append(\
                pd.Series(game_data_frame, index = self.nfl_games_frame.columns), ignore_index = True)
        
        self.nfl_games_frame = fill_dates(self.nfl_games_frame)
