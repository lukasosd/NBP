import requests
from datetime import datetime, timedelta

def cur_import(currency, date):
    while True:
        url = f'https://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}'
        response = requests.get(url)
        if response.status_code == 404:
            date = day_before(date)
        else:
            break

    data = response.json()
    exchange_rate = data['rates'][0]['mid']
    return exchange_rate


def day_before(date):
    date = date.replace('/', '-')
    date = date.replace('.', '-')
    date_time_obj = datetime.strptime(date, '%Y-%m-%d')
    calculation = str(date_time_obj - timedelta(days=1))
    return calculation[:10]

def result(exchange_rate, amount):
    amount = float(amount.replace(',','.'))
    exchange_rate = float(exchange_rate)
    text = f'''Exchange rate:{exchange_rate}
    Calculated amount: {round(amount*exchange_rate,2)}
    '''
    return text