# Betfastaction related constants

BFA_CRED_ROW_IDX = 0
ACCOUNT = "account"
PASSWORD = "password"
BFA_BASE_URL = "https://www.betfastaction.ag"
BFA_LOGIN_URL = BFA_BASE_URL + "/login.aspx"
BFA_MSG_URL = BFA_BASE_URL + "/wager/Message.aspx"
BFA_WELCOME_URL = BFA_BASE_URL + "/wager/Welcome.aspx"
BFA_SPORTS_URL = BFA_BASE_URL + "/wager/CreateSports.aspx"

REQ_PARAMS = (
    ('WT', '0'),
)

NFL_HEADERS = {
    'authority': BFA_BASE_URL,
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': BFA_SPORTS_URL,
    'accept-language': 'en-US,en;q=0.9',
}

NFL_FORM_DATA = {
    '__EVENTTARGET': 'ctl00$WagerContent$idx_1x1',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': '/wEPDwUKLTMxNjc3NTM3NQ9kFgJmD2QWAgIBD2QWCAIDDw8WAh4EVGV4dAUILTEwOC43NSBkZAIHDw8WAh8ABQczMjYuNjggZGQCCw8PFgIfAAUFMC4wMCBkZAIPDw8WAh8ABQc1NjQuNTcgZGRk/r7mzPZbJFDLRhtuuaulB6RJsZo=',
    '__VIEWSTATEGENERATOR': '3DB83FCB',
    '__EVENTVALIDATION': '/wEWqgECobPEowcC/d/+twYC66D1oAECiqWq9AEC/d+Skw8C/92q9g4C++WB0gUC9KCNlgYC9KDBJwLM7MG5BQLyoMH7CwKKpb7PCgL936buBwLplLqkAQLg/Nu6CwKKpdKqAwL937pJAvGg4WAC7KDRhQkC8aDFKgLwoKHPBwLtoJH0DgLvoIHpCwLtoKHEBALxoJkVAu6gjboHAqjPwOkJAsjOwOkJApvmydEFAuyh74cEAoqlxqwGAv3fzqQJAvCgneADAvKgsfEOAuLssWICiqXahw8C/d/i/wECipS6pAEC97jJ/wkC8aq0lQcC18GK/QwCo5S+pQECiqXu4gcC/d/22goC8KDx3wQCiqWCPgL934q2AwKSoaf+CgKKpbbyDgL9356RDAL38tOLBwKKpcrNBwLH3e73DgLxoPmgAQLV98DOBALG3e73DgLyt6noCwLk/a+8CQLVqti/DALW98DOBALF3e73DgK9zs9tAuySwncCsIGwoA8C2Le5+woCi5OStQICsaG79Q0C9MCS1gYCuee1YgKB7eXgDQLT98DOBALE3e73DgLNwraGDgLRwObaBAKKq+zpDgLyoPmnDwKyz4/KBwLuoNHdAQLU98DOBALD3e73DgLC/auVAwK5z/fpDQLC6v30CwKc/NegAwLngoyFAwLHgZiIAwLvwO7cBALs6o2TDQL6t53bAQKA/Y+eAwKpgrT+AgKh/JOjAwKMz9DqDAL0zqvEBwKvwZraBAKT0ISpCwLE6+GYDQLKqrj2DgLl0ITkCgKsgtiHAwLpz5T+BgKtotvoCwLY5amvDQLzt7HUAQKHqsDxDgLYzqvGBwLqgsSDAwKF7K2TDQLY5b2yDQKooYP0CwLMz7z3BwLZzp++BwLTuOHcAQLMqvD4DgKxwcreBAKPofPxCwKj/KehAwKNuP3cAQKSz4CjDgLik+KECQLywMLgBALR98DOBALC3e73DgLEkvaVBQKD/bu/CQKZ5dXEBQK3zpPLBwLxoM2MBgLS98DOBALB3e73DgK9/susAgLsoNmECwLP98DOBALA3e73DgLc/PeUCAKmqqy4DwKOuuGCBQKmqrDdBgLIobOnAgL35eXnAwLQ98DOBAK/3e73DgLPgZjIBgLd98DOBAK+3e73DgLuoM2gAgLe98DOBALH3YLTBwLA5u2zDQKH/tO4CwLC5vW1DQLRgpyJAwLV99SpDQLG3YLTBwLd5umyDQLc5smqDQLW99SpDQLF3YLTBwKr7MGgDQKTwv7gBALT99SpDQLE3YLTBwL0oN3gAQLU99SpDQLD3YLTBwLj/KvsAwLR99SpDQLC3YLTBwK55/31DQLS99SpDcpEMvI/74hslYEJVo6WeyViTi4O'
}
