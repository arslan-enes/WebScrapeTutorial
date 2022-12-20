import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)


def get_data(country):
    df = pd.read_html(f'https://kworb.net/spotify/country/{country}_weekly.html')[0]
    # print(country, pd.read_html(f'https://kworb.net/spotify/country/{country}_weekly.html')[0].shape[0])
    df['country'] = country
    return df


# print(get_data('tr'))

df_all = pd.DataFrame()
for country in ['es', 'fr', 'tr']:
    df_all = df_all.append(get_data(country), ignore_index=True)

print(df_all)
