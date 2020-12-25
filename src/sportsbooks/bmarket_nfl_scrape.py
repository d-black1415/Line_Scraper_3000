import pandas as pd  
import re
import time
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from src.util.helpers import replace_half_with_decimal, retrieve_data_frame_for_game
from src.util.sportsbook_constants.bmrkt_constants import *
from src.credentials.cred_reader import CredentialReader
from src.sportsbooks.sportsbook import SportsBook

class BookieMarket(SportsBook):
    def __init__(self):
        super().__init__()
        self.book_name = 'BookieMarket'
        
    def login_and_retrieve_nfl_page(self):
        bmrkt_creds = CredentialReader.read_cred_row(BMRKT_CRED_ROW_IDX)
        username = bmrkt_creds[0]
        password = bmrkt_creds[1]

        
        chrome_options = Options()  
        chrome_options.add_argument("--headless")  
        
        driver = webdriver.Chrome(executable_path = DRIVER_LOCATION, options = chrome_options)
        driver.implicitly_wait(7)
        driver.get(BMRKT_LOGIN_URL)
        
        driver.find_element_by_xpath(r'//*[@id="Table_01"]/tbody/tr[2]/td[2]/a/img').click()
        driver.switch_to.frame("ifrm")
        driver.find_element_by_xpath(USERNAME_FIELD).send_keys(username)
        driver.find_element_by_xpath(PASSWORD_FIELD).send_keys(password)
        driver.find_element_by_id(SIGN_IN_BUTTON).click()
        driver.find_element_by_xpath(r'/html/body/div[24]/div/div/div[3]/button').click()
        time.sleep(4.5)
        driver.find_element_by_xpath(r'//*[@id="divSportDropdown"]/div/button').click()
        time.sleep(2.5)
        driver.find_element_by_xpath(r'//*[@id="uSportListULDynamic"]/li[5]/b/a').click()
        time.sleep(3.5)
        
        nfl_raw_page = driver.page_source
        driver.quit()
        nfl_page = BeautifulSoup(nfl_raw_page, 'html.parser')
        return nfl_page.find_all(id = re.compile('^LineVersusID'))

    def retrieve_nfl_data_frame(self):
        nfl_page_parsed = self.login_and_retrieve_nfl_page()
        self.nfl_games_frame['MoneyLine'] = ''
        for game in nfl_page_parsed:
            game_frame = retrieve_data_frame_for_game(game, book_name = self.book_name)
            if game_frame.shape[0] > 0:
                self.nfl_games_frame = self.nfl_games_frame.append(game_frame, ignore_index = True)
            else:
                break


