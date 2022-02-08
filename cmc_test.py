from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
import pprint

cmc = CoinMarketCapAPI('YOUR_API_KEY')

ret = cmc.cryptocurrency_listings_latest(cryptocurrency_type='coins')
data = ret.data

list_want_to_know = [
    'BTC', 'ETH', 'ADA', 'SOL', 'DOT', 'ATOM', 'ALGO', 'LUNA'
]

dict_market_cap = {}

for dat in data:
    if dat['symbol'] in list_want_to_know:
        dict_market_cap[dat['symbol']] = dat['quote']['USD']['market_cap']
print('market_cap: ')
pprint.pp(dict_market_cap)

sum_market_cap = sum(dict_market_cap.values())
print(f'sum_market_cap: {sum_market_cap}')

map_market_cap_ratio = {k: (v / sum_market_cap) for k, v in dict_market_cap.items()}
print('map_market_cap_ratio')
pprint.pp(map_market_cap_ratio)
