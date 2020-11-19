import requests
from bs4 import BeautifulSoup
import re
from util.PGW_constants import *

with requests.Session() as s:
    login_resp = s.post(PGW_LOGIN_URL, data = PGW_LOGIN_FORM)
    cookies = login_resp.cookies
    # mess = s.get('https://pgwlines.com/wager/Message.aspx', cookies = cookies)
    nfl_page = s.post(PGW_SPORTS_URL, headers = NFL_HEADERS, params = REQ_PARAMS, data = NFL_FORM_DATA, cookies = cookies)

parsed_nfl_page = BeautifulSoup(nfl_page.text, 'html.parser')
nfl_box = parsed_nfl_page.find_all('tr', class_ = re.compile('TrGame*'))
print(nfl_box[0])
