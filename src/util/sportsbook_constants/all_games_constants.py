ALL_GAMES_CRED_ROW_IDX = 1

ALL_GAMES_LOGIN_URL = r'https://allgames247.com/Security/ValidateCredentials'

ALL_GAMES_NFL_URL = r'https://allgames247.com/Betting/Betting/DefaultGetScheduleDetails'

ALL_GAMES_LOGIN_FORM = {
    'UserName': 'rosie',
    'Password': 'movies'
    }

NFL_HEADERS = {
    'authority': 'allgames247.com',
    'sec-ch-ua': '^\\^Google',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://allgames247.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://allgames247.com/Common/Dashboard',
    'accept-language': 'en-US,en;q=0.9',
}

NFL_FORM_DATA = {
  'Array': 'MQ==',
  'TeaserType': '-1'
}
