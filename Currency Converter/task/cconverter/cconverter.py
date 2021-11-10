import requests as requests


def get_rate():
    print('You received', round(amount / cache[xchange_currency_url][user_currency_code]['rate'], 2),
          f'{xchange_currency_code.upper()}.')


cache = dict()
url_usd = 'http://www.floatrates.com/daily/usd.json'
url_eur = 'http://www.floatrates.com/daily/eur.json'
cache[url_usd] = requests.get(url_usd).json()
cache[url_eur] = requests.get(url_eur).json()
user_currency_code = input().lower()

while True:
    xchange_currency_code = input().lower()
    if xchange_currency_code == '':
        break
    amount = float(input())
    xchange_currency_url = f'http://www.floatrates.com/daily/{xchange_currency_code}.json'

    print('Checking the cache...')

    if xchange_currency_url in cache:
        print('Oh! It is in the cache!')
        get_rate()
    else:
        cache[xchange_currency_url] = requests.get(xchange_currency_url).json()
        print('Sorry, but it is not in the cache!')
        get_rate()
