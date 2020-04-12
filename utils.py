#!/usr/bin/env python
import pandas as pd 
import plotly.express as px
from plotly.offline import init_notebook_mode, iplot 
import plotly.graph_objs as go
import plotly.offline as py
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
import json
import plotly
import plotly.express as px
import warnings
from flask import Flask,render_template,Markup
from datetime import date

import folium

confirmed_col = '#FF5252'
active_col = '#FFA000'
death_col = '#455A64'
rec_col = '#4CAF50'

def get_state_active_df(state_wise):
    df = state_wise.loc[:,['State','Active']]
    df.Active = pd.to_numeric(df.Active)
    df.columns = ['State','Active Cases']
    return df
#w3-bordered w3-border
def create_table(df):
    table=df.to_html(classes='w3-table w3-striped  w3-hoverable w3-white')
    table = table.replace('\n','')
    table = table.replace('dataframe','')
    table = table.replace('border="1"','')
    table = table.replace('style="text-align: right;"','')
    table = table.replace('<th></th>','')
    for i in range(len(df)):
    	table = table.replace('<th>'+str(i)+'</th>','')
    return table

def rev_df(daily_ts):
    latest = daily_ts.sort_values('Total Confirmed',ascending = False)
    latest.reset_index(inplace=True)
    latest = latest.drop('index',axis=1)
    new_ev = latest.loc[0,'Daily Confirmed']
    return new_ev,latest.loc[0,'Total Confirmed']

# ## STATE ACTIVE

def create_state_active(df):
    for i in range(len(df)):
        if(df.loc[i,'Active Cases']==0 or df.loc[i,'Active Cases']==1 or df.loc[i,'Active Cases']==2):
            df = df.drop(i,axis=0)
    fig = px.bar(df.sort_values('Active Cases', ascending=False).sort_values('Active Cases', ascending=True), 
                 y="Active Cases", x="State", 
                 text='Active Cases', 
                 orientation='v',
                range_y = [0, max(df['Active Cases'])+20])
    fig.update_traces(marker_color=active_col, opacity=0.8, textposition='outside')

    fig.update_layout(plot_bgcolor='rgb(230,230,230)',uniformtext_minsize=5, uniformtext_mode='hide',
                      paper_bgcolor='rgba(0,0,0,0)',dragmode=False)
                     
                     #font=dict(family="Courier New, monospace",
                                #size=10,
                                #color="#0f0f0f"),
                    
    #fig.show()

    state_active = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return state_active

# # MAP
#Stamen Toner
def create_map(df):
    ind_coord = pd.read_csv('data/india.csv')
    ind_coord.columns = ['State','Latitude','Longitude','']
    df_full = pd.merge(ind_coord,df,on='State')
    ind_map = folium.Map(location=[20, 80], zoom_start=4.75,tiles='OpenStreetMap',max_zoom=5,min_zoom=4.5,zoom_control=False, no_touch=True)


    for lat, lon, value, name in zip(df_full['Latitude'], df_full['Longitude'], df_full['Active Cases'], df_full['State']):
        folium.CircleMarker([lat, lon],
                            radius=value*0.5,
                            popup = ('<strong>State</strong>: ' + str(name).capitalize() + '<br>'
                                    '<strong>Active Cases</strong>: ' + str(value) + '<br>'),
                            color='red',

                            fill_color='#4CAF50',
                            fill_opacity=0.2 ).add_to(ind_map)
    


    ind_map = ind_map._repr_html_()
    return ind_map


# ## TRENDS

def create_trends(daily_ts):
    daily_ts = daily_ts.drop([i for i in range(32)],axis=0)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=daily_ts['Date'], y=daily_ts['Total Confirmed'],
                        mode='lines+markers',name='Total Cases',line=dict(color=confirmed_col, width=3)))

    fig.add_trace(go.Scatter(x=daily_ts['Date'], y=daily_ts['Total Recovered'], 
                    mode='lines',name='Recovered',line=dict(color=rec_col, width=4)))
    fig.add_trace(go.Scatter(x=daily_ts['Date'], y=daily_ts['Total Active'], 
                    mode='lines',name='Active',line=dict(color=active_col, width=4)))
    fig.add_trace(go.Scatter(x=daily_ts['Date'], y=daily_ts['Total Deceased'], 
                    mode='lines',name='Deaths',line=dict(color=death_col, width=4)))


    fig.update_layout(plot_bgcolor='rgb(230,230,230)',uniformtext_minsize=5, uniformtext_mode='hide',
                      paper_bgcolor='rgba(0,0,0,0)',dragmode=False,
                    
                     legend=dict(x=0,
                                y=1,
                                traceorder="normal",
                                bordercolor="Black",
                                borderwidth=2
                            ))
                      #height=900,width=1500)
    #fig.show()

    trends = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return trends



# ## DAILY TRENDS
def create_daily_cnf(df):
    df = df.drop([i for i in range(32)],axis=0)
    fig = px.bar(df, x="Date", y="Daily Confirmed",text='Daily Confirmed', barmode='group')
    fig.update_traces(marker_color=confirmed_col, opacity=0.8, textposition='outside')
    fig.update_layout(plot_bgcolor='rgb(230,230,230)',uniformtext_minsize=5, uniformtext_mode='hide',
                      paper_bgcolor='rgba(0,0,0,0)',dragmode=False)
                      #height=900,width=1500)
    #fig.show()
    new_cases_per_day = map_html = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return new_cases_per_day

def create_daily_rec(df):
    df = df.drop([i for i in range(32)],axis=0)
    fig = px.bar(df, x="Date", y="Daily Recovered",text='Daily Recovered', barmode='group')
    fig.update_traces(marker_color=rec_col, opacity=0.8, textposition='outside')
    fig.update_layout(plot_bgcolor='rgb(230,230,230)',uniformtext_minsize=5, uniformtext_mode='hide',
                      paper_bgcolor='rgba(0,0,0,0)',dragmode=False
                      )
                      #height=900,width=1500)
    #fig.show()
    new_cases_per_day = map_html = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return new_cases_per_day


