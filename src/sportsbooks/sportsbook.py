from abc import ABC, abstractmethod

import pandas as pd
import numpy as np

class SportsBook(ABC):

    def __init__(self):
        self.nfl_games_frame = pd.DataFrame(columns=['Month', 'Day', 'Team_ID', 'Internal_ID', 'Team', 'Spread',
                                                     'Spread_Line', 'Total', 'Total_Line'])

    @abstractmethod
    def login_and_retrieve_nfl_page(self):
        pass

    # Extract data frames for each NFL game
    @abstractmethod
    def retrieve_nfl_data_frame(self):
        pass
    
    def __str__(self):
        return 'NFL Frame for book: {}\n {}'.format(self.book_name, self.nfl_games_frame)
