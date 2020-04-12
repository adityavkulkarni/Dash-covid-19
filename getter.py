import requests
import urllib
import pandas as pd

def define_total(total_):
    dict = {'confirmed':total_['confirmed'],
            'recovered':total_['recovered'],
            'deaths':total_['deaths'],
            'active':total_['active'],
            'last_updated':total_['lastupdatedtime'],
	    'delta':total_['deltaconfirmed']
           }
    return(dict)

url = 'https://api.covid19india.org/data.json'
print("Getting Response") 
res = requests.get(url)
ts = res.json()['cases_time_series']
cols =list(ts[0].keys())
cols
data = []
for t in ts:
    dat = []
    for col in cols:
        dat.append(t[col])
    data.append(dat)
daily_ts = pd.DataFrame(data,columns=cols)
daily_ts.columns = ['Daily Confirmed','Daily Deceased','Daily Recovered','Date','Total Confirmed','Total Deceased','Total Recovered']
daily_ts['Total Active'] = pd.to_numeric(daily_ts['Total Confirmed']) - pd.to_numeric(daily_ts['Total Recovered'])-pd.to_numeric(daily_ts['Total Deceased'])
print("Downloaded Daily Data")

st = res.json()['statewise']
cols =list(st[0].keys())
data = []
for t in st:
    dat = []
    for col in cols:
        dat.append(t[col])
    data.append(dat)
state_wise = pd.DataFrame(data,columns=cols)
#state_wise = state_wise.drop('delta',axis = 1)
total_ = state_wise.loc[0,:]
state_wise = state_wise.drop(0,axis=0)
state_wise.reset_index(inplace=True)
state_wise = state_wise.drop(['index'],axis=1)
state_wise = state_wise.drop(['statecode','deltaconfirmed', 'deltadeaths',
       'deltarecovered'],axis=1)
print(state_wise.columns)
state_wise.columns =['Active','Confirmed','Deaths','Last_Updated_Time','Recovered','State']
state = pd.DataFrame()
state['State']=state_wise['State']
state['Confirmed']=state_wise['Confirmed']
state['Active']=state_wise['Active']
state['Recovered']=state_wise['Recovered']
state['deaths']=state_wise['Deaths']

print("Downloaded State-wise Data")

total = define_total(total_)
total = pd.DataFrame(total.items())
total = total.transpose()
total.columns = total.loc[0,:]
total = total.drop(0,axis=0)

print("Getting Total")
daily_ts.to_csv('data/google/daily_ts.csv')
print("Written Daily Data")
state.to_csv('data/google/state_wise.csv')
print("Written State-wise Data")
total.to_csv('data/google/total.csv')
print("Writen Total Data")
