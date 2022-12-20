import pandas as pd
import requests
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

print(pd.read_html('https://www.coingecko.com/tr?page=1'))
