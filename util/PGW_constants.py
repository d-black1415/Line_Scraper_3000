# PGW related constants

PGW_BASE_URL = "https://pgwlines.com/"
PGW_LOGIN_URL = PGW_BASE_URL + '/default.aspx'
PGW_SPORTS_URL = PGW_BASE_URL + "/wager/CreateSports.aspx"
ACCOUNT = 'ctl00$MainContent$ctlLogin$_UserName'
PASSWORD = 'ctl00$MainContent$ctlLogin$_Password'


PGW_LOGIN_FORM = {
  '__EVENTTARGET': '',
  '__EVENTARGUMENT': '',
  '__VIEWSTATE': '/wEPDwUENTM4MWQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFJGN0bDAwJE1haW5Db250ZW50JGN0bExvZ2luJEJ0blN1Ym1pdH0HpK9E6CXKnHk9NvkOvX5k8O7z',
  '__VIEWSTATEGENERATOR': 'CA0B0334',
  '__EVENTVALIDATION': '/wEWBgKV6qGECgL4lt/gCgLHhaW/AwLIlrvGCgLZh4jSAQKMseCTDpQNr+9u7/z7mDzubxcNh8OxEz4q',
  'ctl00$MainContent$ctlLogin$_UserName': 'Rosie',
  'ctl00$MainContent$ctlLogin$_Password': 'magic',
  'ctl00$MainContent$ctlLogin$BtnSubmit.x': '44',
  'ctl00$MainContent$ctlLogin$BtnSubmit.y': '25',
  'ctl00$MainContent$ctlLogin$_IdBook': '25',
  'ctl00$MainContent$ctlLogin$Redir': ''
}

NFL_HEADERS = {
    'authority': PGW_BASE_URL,
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'image',
    'accept-language': 'en-US,en;q=0.9',
    'referer': PGW_SPORTS_URL
}

REQ_PARAMS = (
    ('WT', '0'),
)

NFL_FORM_DATA = {
  '__EVENTTARGET': '',
  '__EVENTARGUMENT': '',
  '__VIEWSTATE': '/wEPDwUKLTMxNjc3NTM3NQ9kFgJmD2QWAgIDD2QWAgIBD2QWCgIBDw8WAh4EVGV4dAUCMCBkZAIDDw8WAh8ABQI5IGRkAgUPDxYCHwAFBDk5MSBkZAIHDw8WAh8ABQEwZGQCCQ8PFgIfAAUCMCBkZGRmHEDyJPb+UaOen3nyVSfSqmeHNA==',
  '__VIEWSTATEGENERATOR': '3DB83FCB',
  '__EVENTVALIDATION': '/wEWGwKY/8HbBwL93/63BgLqlbKLCQL935KTDwLqlZ4wAv3fpu4HAuqVitUHAv3fukkC6pWW0wQC/d/OpAkC6pWC+AsC/d/i/wEC6pXunAMC/d/22goC6pXawQoC/d+KtgMC6pWmjQwC/d+ekQwC6pWSsgMCx93u9w4CibPh/Q4Cxt3u9w4CirPh/Q4Cxd3u9w4Ci7Ph/Q4CxN3u9w4CjLPh/Q7xJH60RuMzbEHKSDUtGMODkcpLEA==',
  'lg_229': '229',
  'ctl00$WagerContent$btn_Continue1': 'Continue'
}

NUM_COLS = 9

DATE_IDX = 1
TEAM_ID_IDX = 2
TEAM_IDX = 3
SPREAD_IDX = 4
TOTAL_IDX = 5
