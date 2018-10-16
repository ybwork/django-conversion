import requests

app_id = '154f24f80882454da1d7f059fa926c7f'


def get_rates(from_currency, to_currencies):
    params = {'app_id': app_id, 'base': from_currency, 'symbols': to_currencies}
    req = requests.get('https://openexchangerates.org/api/latest.json', params=params)
    data = req.json()
    return data['rates']

    # data['rates']['AED']
    # for val in data['rates']:
    #     print(data['rates'][val])