FALCON_BASE_URL = 'https://backend.falcon.ag'
FALCON_LOGIN_URL = FALCON_BASE_URL + '/Login.aspx'
FALCON_NFL_URL = FALCON_BASE_URL + '/wager/NewScheduleHelper.aspx'
FALCON_CRED_ROW_IDX = 2
FALCON_LINE_INFO = 'GameLines'

FALCON_LOGIN_FORM = {
  'IdBook': '1',
  'Redir': '',
}

NFL_HEADERS = {
    'authority': 'backend.falcon.ag',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://backend.falcon.ag/wager/NewScheduleR.aspx?lg=544&WT=0',
    'accept-language': 'en-US,en;q=0.9',
}

REQ_PARAMS = (
    ('WT', '0'),
    ('lg', '544'),
)

