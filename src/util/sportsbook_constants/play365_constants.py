PLAY365_CREDS_ROW_IDX = 4

PLAY365_LOGIN_URL = r'https://engine.play365.ag/login.aspx'

PLAY365_NFL_URL = r'https://engine.play365.ag/wager/betslip/getLinesbyLeague.asp'

PLAY365_LOGIN_FORM_DATA = {
  'IdBook': '4',
  'Redir': '',
  'IdBook': '',
}

NFL_HEADERS = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://engine.play365.ag',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://engine.play365.ag/wager/Sports.aspx?WT=0&lid=69',
    'Accept-Language': 'en-US,en;q=0.9',
}

NFL_DATA = {
  'pid': '262519',
  'aid': '13136',
  'idp': '2061',
  'idpl': '3693',
  'idc': '64170148',
  'idlt': '20',
  'idls': 'E',
  'idl': '69',
  'nhll': 'A',
  'mlbl': 'W',
  'utc': '-8',
  'idlan': '0',
  'bid': '4',
  'wt': '0',
  'wtid': '0'
}

REGEX_GAME_FINDER = 'row (odd|even)'