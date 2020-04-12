from utils import get_state_active_df,rev_df,create_map,create_state_active, create_trends,create_daily_cnf,create_daily_rec,create_table
import pandas as pd
#state_wise,daily_ts,total = create_csv()

#create_csv()
state_wise = pd.read_csv('data/google/state_wise.csv')
daily_ts = pd.read_csv('data/google/daily_ts.csv')
total = pd.read_csv('data/google/total.csv')


df = get_state_active_df(state_wise)
new_t = total['delta']
#new_ev,yest = rev_df(daily_ts)
#new_t = int(total.loc[0,'confirmed']) - int(yest)
ind_map = create_map(df)
state_active = create_state_active(df)
trend  = create_trends(daily_ts)
daily_cnf = create_daily_cnf(daily_ts)
daily_rec = create_daily_rec(daily_ts)
tab1 = state_wise
for i in range(len(tab1)):
	if(tab1.loc[i,'Confirmed']==0 ):
		    tab1 = tab1.drop(i,axis=0)
tab1 = tab1.sort_values('Confirmed',ascending=False)
tab1.reset_index(inplace=True)
tab1 = tab1.drop('index',axis=1)
tab = create_table(tab1.drop('Unnamed: 0',axis=1))

from flask import Flask,render_template,Markup
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('trial.html',date = total.loc[0,'last_updated'],
                           new_cases = int(new_t),
                           total_confirmed = total.loc[0,'confirmed'],
                           active_cases = total.loc[0,'active'],
                           deaths = total.loc[0,'deaths'],
                           cured_cases = total.loc[0,'recovered'],
                           trends = trend,
                           state = state_active,
                           dl_cnf = daily_cnf,
                           dl_rec = daily_rec,
                           table = Markup(tab),
                           map_ind = Markup(ind_map))
if __name__ == "__main__":
    app.run(port=5000)

