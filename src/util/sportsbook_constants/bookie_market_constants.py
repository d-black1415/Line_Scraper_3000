BM_BASE_URL = 'https://www.bookiemarket.com'
BM_LOGIN_URL = BM_BASE_URL + '/splashscreen/bookiemarket/LOGIN/playerlogin.aspx'

BOOKIE_MARKET_ROW_IDX = 3

BM_LOGIN_FORM = {
    'btnSignIn': 'Sign In'
}

BM_HEADERS = {
    'authority': 'awsome.77711.eu',
    'Accept': 'application/json',
    'x-requested-with': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
    'origin': 'https://awsome.77711.eu',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://awsome.77711.eu/fd/defaultfd?player=1&loginfrom=https%3a%2f%2fwww.bookiemarket.com&G=fe827f9a-14b9-44ab-8b67-9f2c5540d93d&U=299133',
    'accept-language': 'en-US,en;q=0.9',
    'Authorization': 'Basic Og==',
    'Content-Type': 'application/json; charset=utf-8'
}

BM_DATA_JSON = {
    'sUserID': '299133',
    'sLink': '38,True,False,False,0',
    'sTeamID': '',
    'sClearCache': 'false',
    'sEventRefreshStringOG': ''
}

BM_NFL_URL = 'https://awsome.77711.eu/WebService.asmx/LinesGetAllLines'

BM_PARAMS = (
    ('player', '1'),
    ('loginfrom', BM_BASE_URL),
    ('G', 'fe827f9a-14b9-44ab-8b67-9f2c5540d93d'),
    ('U', '299133'),
)
