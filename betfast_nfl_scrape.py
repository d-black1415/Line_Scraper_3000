import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
data = {"User":"stevengfan","password":"boopool"}

cookies = {
    'Cookie-Sport-Selection': '%7B%22SOCCER%20-%20EUROPE%22%3A%221%22%2C%22FOOTBALL%22%3A%221%22%2C%22FOOTBALL%20-%20FUTURES%22%3Anull%2C%22GOLF%22%3Anull%2C%22AUTO%20RACING%22%3Anull%2C%22FOOTBALL%20-%20PROPS%22%3Anull%2C%22LIVE%20IN%20-%20PLAY%22%3Anull%2C%22SOCCER%20PROPS%22%3Anull%2C%22MIXED%20MARTIAL%20ARTS%22%3Anull%7D',
    '__cfduid': 'db14c8ef95994b1bbce08ed6d9075f9e31603488273',
    'ASP.NET_SessionId': '3uutpvzedmqacfrsbmn3cknd',
    'pl': '',
}

message_headers = {
    'authority': 'www.betfastaction.ag',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.betfastaction.ag/',
    'accept-language': 'en-US,en;q=0.9',
}

Welcome_headers = {
    'authority': 'www.betfastaction.ag',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.betfastaction.ag/wager/Message.aspx',
    'accept-language': 'en-US,en;q=0.9',
}

cs_headers = {
    'authority': 'www.betfastaction.ag',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.betfastaction.ag/wager/Welcome.aspx',
    'accept-language': 'en-US,en;q=0.9',
}

params = (
    ('WT', '0'),
)

nfl_headers = {
    'authority': 'www.betfastaction.ag',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'origin': 'https://www.betfastaction.ag',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.betfastaction.ag/wager/CreateSports.aspx?WT=0',
    'accept-language': 'en-US,en;q=0.9',
}

nfl = {
  '__EVENTTARGET': 'ctl00$WagerContent$idx_1x1',
  '__EVENTARGUMENT': '',
  '__VIEWSTATE': '/wEPDwUKLTMxNjc3NTM3NQ9kFgJmD2QWAgIBD2QWCAIDDw8WAh4EVGV4dAUILTEwOC43NSBkZAIHDw8WAh8ABQczMjYuNjggZGQCCw8PFgIfAAUFMC4wMCBkZAIPDw8WAh8ABQc1NjQuNTcgZGRk/r7mzPZbJFDLRhtuuaulB6RJsZo=',
  '__VIEWSTATEGENERATOR': '3DB83FCB',
  '__EVENTVALIDATION': '/wEWqgECobPEowcC/d/+twYC66D1oAECiqWq9AEC/d+Skw8C/92q9g4C++WB0gUC9KCNlgYC9KDBJwLM7MG5BQLyoMH7CwKKpb7PCgL936buBwLplLqkAQLg/Nu6CwKKpdKqAwL937pJAvGg4WAC7KDRhQkC8aDFKgLwoKHPBwLtoJH0DgLvoIHpCwLtoKHEBALxoJkVAu6gjboHAqjPwOkJAsjOwOkJApvmydEFAuyh74cEAoqlxqwGAv3fzqQJAvCgneADAvKgsfEOAuLssWICiqXahw8C/d/i/wECipS6pAEC97jJ/wkC8aq0lQcC18GK/QwCo5S+pQECiqXu4gcC/d/22goC8KDx3wQCiqWCPgL934q2AwKSoaf+CgKKpbbyDgL9356RDAL38tOLBwKKpcrNBwLH3e73DgLxoPmgAQLV98DOBALG3e73DgLyt6noCwLk/a+8CQLVqti/DALW98DOBALF3e73DgK9zs9tAuySwncCsIGwoA8C2Le5+woCi5OStQICsaG79Q0C9MCS1gYCuee1YgKB7eXgDQLT98DOBALE3e73DgLNwraGDgLRwObaBAKKq+zpDgLyoPmnDwKyz4/KBwLuoNHdAQLU98DOBALD3e73DgLC/auVAwK5z/fpDQLC6v30CwKc/NegAwLngoyFAwLHgZiIAwLvwO7cBALs6o2TDQL6t53bAQKA/Y+eAwKpgrT+AgKh/JOjAwKMz9DqDAL0zqvEBwKvwZraBAKT0ISpCwLE6+GYDQLKqrj2DgLl0ITkCgKsgtiHAwLpz5T+BgKtotvoCwLY5amvDQLzt7HUAQKHqsDxDgLYzqvGBwLqgsSDAwKF7K2TDQLY5b2yDQKooYP0CwLMz7z3BwLZzp++BwLTuOHcAQLMqvD4DgKxwcreBAKPofPxCwKj/KehAwKNuP3cAQKSz4CjDgLik+KECQLywMLgBALR98DOBALC3e73DgLEkvaVBQKD/bu/CQKZ5dXEBQK3zpPLBwLxoM2MBgLS98DOBALB3e73DgK9/susAgLsoNmECwLP98DOBALA3e73DgLc/PeUCAKmqqy4DwKOuuGCBQKmqrDdBgLIobOnAgL35eXnAwLQ98DOBAK/3e73DgLPgZjIBgLd98DOBAK+3e73DgLuoM2gAgLe98DOBALH3YLTBwLA5u2zDQKH/tO4CwLC5vW1DQLRgpyJAwLV99SpDQLG3YLTBwLd5umyDQLc5smqDQLW99SpDQLF3YLTBwKr7MGgDQKTwv7gBALT99SpDQLE3YLTBwL0oN3gAQLU99SpDQLD3YLTBwLj/KvsAwLR99SpDQLC3YLTBwK55/31DQLS99SpDcpEMvI/74hslYEJVo6WeyViTi4O'
}

#Start Requests Session and navigate to NFL page
with requests.Session() as s:
    p = s.post("https://www.betfastaction.ag/login.aspx", data = data)
    mes = s.get('https://www.betfastaction.ag/wager/Message.aspx', headers=message_headers, cookies=cookies)
    wel = s.get('https://www.betfastaction.ag/wager/Welcome.aspx', headers=Welcome_headers, cookies=cookies)
    screen = s.get('https://www.betfastaction.ag/wager/CreateSports.aspx', headers=cs_headers, params=params, cookies=cookies)
    foot = s.post('https://www.betfastaction.ag/wager/CreateSports.aspx', headers=nfl_headers, params=params, cookies=cookies, data=nfl)
    
    #Store nfl page in BeautifulSoup object
    foot_table = BeautifulSoup(foot.text,'html.parser')

final_table = foot_table.find('table')
print(final_table)
games = final_table.find_all('tr', {'class': re.compile('TrGame.*')})

#Need to figure out how to parse through html with structured solution for robust repeatability
