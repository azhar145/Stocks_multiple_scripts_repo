from yahoo_fin import options 
import pandas as pd
from yahoo_fin import stock_info as f
import textwrap 
#pd.set_option("max_colwidth", 12)
from yahoo_fin import news as g
import html5lib
import numpy as np 
from numerize import numerize 
import sys

pd.options.display.max_columns = 50
pd.options.display.max_rows = 1000
#pd.options.display.max_colwidth =180
pd.set_option('display.max_colwidth', 16)
pd.set_option("display.expand_frame_repr", False)

#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.width',15)
#pd.set_option('display.max_colwidth', -1)
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")



dd_most_active=pd.DataFrame(f.get_day_most_active())

#dd_most_active['Volume']=numerize.numerize(dd_most_active['Volume'])

dd_most_active['%_Vol_delta']=100*(dd_most_active['Volume']/dd_most_active['Avg Vol (3 month)'])-100
dd_most_active['%_Vol_delta']=dd_most_active['%_Vol_delta'].round(2)
print('---------------  Most Active -----------------------')
#print(dd_most_active['Volume'])
########################################################
#dd_most_active['Volume']=dd_most_active['Volume']*100000000
#a = numerize.numerize(dd_most_active['Volume'][0])

#print(a)
#############################################################
#dd_most_active['Volume']=numerize.numerize(dd_most_active['Volume']).any()

dd_most_active=dd_most_active.sort_values(by=['Volume'], ascending=False)
#dd_most_active=dd_most_active.sort_values(by=['Change'], ascending=False)



for x in dd_most_active.index:
        dd_most_active['Volume'].loc[x]=numerize.numerize(np.float32(dd_most_active['Volume'].loc[x]).item())
        dd_most_active['Avg Vol (3 month)'].loc[x]=numerize.numerize(np.float32(dd_most_active['Avg Vol (3 month)'].loc[x]).item())
        if 'T' not in str(dd_most_active['Market Cap'].loc[x]):
            dd_most_active['Market Cap'].loc[x]=numerize.numerize(np.float32(dd_most_active['Market Cap'].loc[x]).item())

print(dd_most_active)



print('\n\n',' *************** Day Active *****************','\n\n')


#sys.exit()



#dd_most_active['Volume']=dd_most_active['Volume']*100000000


#f5.to_csv('/home/ec2-user/environment/x3/stocks/x4/output55.txt',sep=' ',mode='w+',header=True)
#f5.to_html(buf='/home/ec2-user/environment/x3/stocks/x4/output55.html', columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, max_rows=None, max_cols=None, show_dimensions=False, decimal='.', bold_rows=True, classes=None, escape=True, notebook=False, border=None, table_id=None, render_links=False, encoding=None)

print('---------------------- Day Gainers ---------------------')        
dd_day_gainers=pd.DataFrame(f.get_day_gainers())
dd_day_gainers['%_Vol_delta']=100*(dd_day_gainers['Volume']/dd_day_gainers['Avg Vol (3 month)'])-100
dd_day_gainers['%_Vol_delta']=dd_day_gainers['%_Vol_delta'].round(2)

#print(dd_day_gainers.columns)   


for x in dd_day_gainers.index:
        dd_day_gainers['Volume'].loc[x]=numerize.numerize(np.float32(dd_day_gainers['Volume'].loc[x]).item())
        dd_day_gainers['Avg Vol (3 month)'].loc[x]=numerize.numerize(np.float32(dd_day_gainers['Avg Vol (3 month)'].loc[x]).item())
        if 'T' not in str(dd_day_gainers['Market Cap'].loc[x]):
            dd_day_gainers['Market Cap'].loc[x]=numerize.numerize(np.float32(dd_day_gainers['Market Cap'].loc[x]).item())

f2=dd_day_gainers.sort_values(by=['Change'], ascending=False)
print(dd_day_gainers.sort_values(by=['Change'], ascending=False))
print('\n\n')

#f2.to_csv('/home/ubuntu/environment/stocks/x5/output55.txt',sep=' ',mode='w')
#print('\n\n',' *************** Day Gainers *****************','\n\n')

print('---------------------- Day Losers  ---------------------')        
dd_day_losers=pd.DataFrame(f.get_day_losers())
dd_day_losers['%_Vol_delta']=100*(dd_day_losers['Volume']/dd_day_losers['Avg Vol (3 month)'])-100
dd_day_losers['%_Vol_delta']=dd_day_losers['%_Vol_delta'].round(2)


for x in dd_day_losers.index:
        dd_day_losers['Volume'].loc[x]=numerize.numerize(np.float32(dd_day_losers['Volume'].loc[x]).item())
        dd_day_losers['Avg Vol (3 month)'].loc[x]=numerize.numerize(np.float32(dd_day_losers['Avg Vol (3 month)'].loc[x]).item())
        if 'T' not in str(dd_day_losers['Market Cap'].loc[x]):
                        dd_day_losers['Market Cap'].loc[x]=numerize.numerize(np.float32(dd_day_losers['Market Cap'].loc[x]).item())

f3=dd_day_losers.sort_values(by=['Change'], ascending=True)
print(dd_day_losers.sort_values(by=['Change'], ascending=True))


#f3.to_csv('/home/ubuntu/environment/stocks/x5/output55.txt',sep=' ',mode='w')
##print('\n\n',' *************** Day Losers *****************','\n\n')

#########################################################################
####################################################

print('\n\n')

ticker=input("Enter ticker: ")

#ticker='^ndx'
x="calls"
y="puts"

##########################################################################################################
print('\n\n')
print(" haha more to the story")
print('dd quote table -----> ',f.get_quote_data(ticker)['symbol'])
print('dd quote table -----> ',f.get_quote_data(ticker)['shortName'])
print('stock live  price ------ >  ',f.get_live_price(ticker))
#print('stock postmarket price ------ >  ',f.get_quote_data(ticker)['postMarketPrice'])
print('Yesterday_close ---->   ',f.get_quote_data(ticker)['regularMarketPreviousClose'])
#print('stock pre market price ---> ',f.get_premarket_price(ticker).round(2))
#print('stock post market price ----> ',f.get_postmarket_price(ticker))
print('stock market status ---> ',f.get_market_status())
print('dd regularMarketVolume----> ', f.get_quote_data(ticker)['regularMarketVolume']/1000000, 'Million')
print('dd averageDailyVolume10Day----> ', f.get_quote_data(ticker)['averageDailyVolume10Day']/1000000, 'Million')
print('dd averageDailyVolume3Mont ----> ', f.get_quote_data(ticker)['averageDailyVolume3Month']/1000000, 'Million')
print('dd averageAnalystRating ----> **************** ', f.get_quote_data(ticker)['averageAnalystRating'])

print("where problem is")




print('dd Next Earning Date --------> ',f.get_next_earnings_date(ticker))
print('dd Days range ------> ',f.get_quote_data(ticker)['regularMarketDayRange'])
############# below is long
print('dd quote table -----> ',f.get_quote_data(ticker))
m=f.get_holders(ticker)
print('dd holders ----> ',m)
print('\n\n\n')
#########################################################################
print("Volume up or down - (current volume vs 10 days volume),(current volume vs last 3 months)")

if (f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume10Day']) < 0:
    print('22 ----> 10 days (volume low yest vs last 10days)',(f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume10Day']))

if (f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume10Day']) >  0:
        print('22 ----> 10 days (volume high yest vs last 10days)',(f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume10Day']))

if (f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume3Month']) < 0:
        print('22 ----> 3 mnths (volume low yest vs last 3mnths)',(f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume3Month']))

if (f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume3Month']) >  0:
                    print('22 ----> 3 mnths (volume high yest vs last 3mnths)',(f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume3Month']))
####################################################
##########################################################
#if (f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume10Day'])/1000000)) > 0:
#    print('22 ----> 10 days (high)',(f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume10Day'])
##    print('22 ----> 3 mnths (high)',(f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume3Month'])/1000000)
#else: (f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume10Day'])/1000000)) < 0:  
#    print('22 ----> 10 days (low)',(f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume10Day'])
##    print('22 ----> 3 mnths (low)',(f.get_quote_data(ticker)['regularMarketVolume'])-(f.get_quote_data(ticker)['averageDailyVolume3Month'])/1000000)
################################################
print('\n')
print('23 ----> ',f.get_stats(ticker))
print('\n')
print('24 ----> ',f.get_stats_valuation(ticker))
print('\n')
print('Analysts ---->  ',f.get_analysts_info(ticker))
print('\n\n')
###########################################################################################################
sys.exit()


nflx_dates = options.get_expiration_dates(ticker)
chain = options.get_options_chain(ticker)
chain[x]

#######################################################
c=chain[x]
#print(c)
df=pd.DataFrame(c)
print(df.shape)
#dfc=df.sort_values(by='Volume')
dfc=df.sort_values(by='Volume', ascending=False)
#print(df)
#print(dfa.Date.dt.date.unique())
print('*****************************************************************************************************')
print("calls")
print(dfc.head(4))
print('*****************************************************************************************************')
print('\n\n')
#######################################################
#######################################################
p=chain[y]
#print(c)
df=pd.DataFrame(p)
print('*****************************************************************************************************')
print(df.shape)
dfp=df.sort_values(by='Volume', ascending=False)
#print(df)
#print(dfa.Date.dt.date.unique())
print("puts")
print(dfp.head(4))
print('*****************************************************************************************************')
print('\n\n')
nflx_dates= options.get_expiration_dates(ticker)
print(nflx_dates)

################################################################################
dfd=pd.DataFrame()
#dfd=get_puts(ticker, '06/11/2021')
#print(dfd)




'''
info = {}
for date in nflx_dates:
        info[date] = options.get_options_chain(ticker)
#print(info)
#print(info.Date.dt.date.unique())



chain["puts"]
options.get_options_chain("nflx", "April 26, 2019")
 
options.get_options_chain("nflx", "05/03/19")
 
options.get_options_chain("nflx", "05/10/2019")
options.get_calls("nflx")
 
options.get_calls("nflx", "04/26/19")
 
 
options.get_puts("nflx")
 
options.get_puts("nflx", "04/26/19")



####################################################
#How to get options data for each expiration date

nflx_dates= options.get_expiration_dates("nflx")
 
info = {}
for date in nflx_dates:
    info[date] = options.get_options_chain("nflx")
    
info["October 18, 2019"]

##################################################

# How to get options data for every stock in the Dow
from yahoo_fin import stock_info as si
 
dow_tickers = si.tickers_dow()
 
# replace DOW with DWDP in ticker list
dow_tickers.remove("DOW")
dow_tickers.append("DWDP")
 
# scrape the options data for each Dow ticker
dow_data = {}
for ticker in dow_tickers:
    try:
        dow_data[ticker] = options.get_options_chain(ticker)
    except Exception:
        print(ticker + " failed")
        
        
dow_data["AAPL"]["calls"]
 
dow_data["WMT"]["calls"]

'''
dd=pd.DataFrame(g.get_yf_rss(ticker))
#mm=dd.iloc[:5,[0,7,8,9,10,12,13]]

#dd.to_csv('/home/ec2-user/environment/x3/stocks/x4/output55.txt',sep=' ')

'''
print(dd.iloc[:5,[0,7,8,9,10,12,13]])
#mm.to_csv(r'/home/ec2-user/environment/x3/stocks/x4/output.txt', index=None, sep=' ', mode='w+')
print("kkkkk")
dd.to_csv('/home/ec2-user/environment/x3/stocks/x4/output.txt',sep=' ')
####import np
##np.savetxt(r'/home/ec2-user/environment/x3/stocks/x4/output.txt',mm.values, fmt='%d')
'''
print('Most_acive_volume.py completed')
