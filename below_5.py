import coinmarketcap as cmc
from coinmarketcap import Market
import json
import pandas as pd
#from slackclient import SlackCient
import os

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

coinmarketcap = Market()
a = coinmarketcap.ticker(convert='INR')
Currencies = pd.DataFrame(a, dtype='float')
Currencies.set_index(['name','symbol'], inplace = True )

Curr_5 = Currencies[( -5 < Currencies.percent_change_1h )&(Currencies.percent_change_1h > 0) &(Currencies['rank'] <= 20)].sort_values('percent_change_1h', ascending = False)
# print(Curr_5)
if not Curr_5.empty:
    for i,d in Curr_5.iterrows():
        notify(title = str(i[0]) +' ' +i[1],
        subtitle = 'is down %f percent'%(d.percent_change_1h),
        message  = 'at %f btc' %(d.price_btc))
