# Contents of ~/my_app/main_page.py
import streamlit as st
import pandas as pd
import pymongo
#import pymongo[srv]
from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import plotly.express as px

st.set_page_config(layout="wide")

st.markdown("# Stonkolawdhavemercy 🚀💩🔞🚭☠︎🤯💥")
st.sidebar.markdown("# Testsite 🚀💩🔞🚭☠︎🤯💥")

# streamlit_app.py

#@st.cache(hash_funcs={MongoClient: id})
def get_client():
    return MongoClient(**st.secrets["mongo"])

client = get_client()
db = client.stonks

@st.experimental_memo
def givestonks():
    collection = db.overall2
    overall = collection.find()
    df = pd.DataFrame(overall)
    df = df.drop(columns=['_id'])
    df = df.drop(columns=[' CUSIP'])
    df = df.drop(columns=['   CIK'])
    df = df.astype({" IPO Date": str})
    #df = df.astype({" Industry": str})
    df = df[['Overall points', 'Market Capitalization size','Name', 'Ticker', 'Dividend points normal', 'Revenues points normal', 'Free Cash Flow points normal', 'Net Income points normal',
     'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 'Payout Ratio points normal'#, 'Website'
        ]]

    #df = df.loc[df[' Industry'] == industry]
    #df = df.drop(columns=[' Industry'])


    df25 = df.head(25)
    df25 = df25.sort_values(by=['Overall points'], ascending=True)

    df = df.astype({"Name": str})

    return df, df25

full = givestonks()[0]
top25 = givestonks()[1]

st.write(full)

#collection = db.overall2
#data = collection.find()
#data1 = (data.index += 1 )

#df = pd.DataFrame(data)
#df = df.drop(columns=['_id'])
#df = df.drop(columns=[' CUSIP'])
#df = df.drop(columns=['   CIK'])
#df = df.astype({" IPO Date": str})

weightrev = st.slider('Weight for Revenue', 1, 10, 1)
weightdiv = st.slider('Weight for Dividends', 1, 10, 1)
weightfcf = st.slider('Weight for FCF', 1, 10, 1)
weightni = st.slider('Weight for Net Income', 1, 10, 1)
weightnim = st.slider('Weight for Net Income Margin', 1, 10, 1)
weightcr = st.slider('Weight for Current Ratio', 1, 10, 1)
weightos = st.slider('Weight for Outstanding shares', 1, 10, 1)
weightpr = st.slider('Weight for Payout Ratio', 1, 10, 1)

full['Revenues points normal'] = full['Revenues points normal']*weight
full['Dividend points normal'] = full['Dividend points normal']*weight
full['Free Cash Flow points normal'] = full['Free Cash Flow points normal']*weight
full['Net Income points normal'] = full['Net Income points normal']*weight
full['Net Income Margin points normal'] = full['Net Income Margin points normal']*weight
full['Current Ratio points normal'] = full['Current Ratio points normal']*weight
full['Weighted Average Shares (Diluted) points normal'] = full['Weighted Average Shares (Diluted) points normal']*weight
full['Payout Ratio points normal'] = full['Payout Ratio points normal']*weight

full['Overall points'] = full['Overall points']+(full['Revenues points normal']-(full['Revenues points normal']/weight)) + (full['Dividend points normal']-(full['Dividend points normal']/weight)) + (full['Free Cash Flow points normal']-(full['Free Cash Flow points normal']/weight)) + (full['Net Income points normal']-(full['Net Income points normal']/weight)) + (full['Net Income Margin points normal']-(full['Net Income Margin points normal']/weight)) + (full['Current Ratio points normal']-(full['Current Ratio points normal']/weight)) + (full['Weighted Average Shares (Diluted) points normal']-(full['Weighted Average Shares (Diluted) points normal']/weight)) + (full['Payout Ratio points normal']-(full['Payout Ratio points normal']/weight))

full = full.sort_values(by=['Overall points'], ascending=False)
full = full.reset_index(drop=True)

#df3['Overall points2'] = df3['Revenues points normal'] + df3['Dividend points normal'] 
#+ df3['Free Cash Flow points normal'] + df3['Net Income points normal'] + df3['Net Income Margin points normal'] + df3['Current Ratio points normal']
#+ df3['Weighted Average Shares (Diluted) points normal'] + df3['Payout Ratio points normal']

df20 = full.head(20)
df20 = df20.sort_values(by=['Overall points'], ascending=True)

fig = px.bar(df20, x=["Dividend points normal", "Revenues points normal", "Free Cash Flow points normal", 'Net Income points normal', 
                    'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 
                    'Payout Ratio points normal'], y="Name", title="Stocks sorted by average overall points broken down my metric",
            labels=dict(value="Average overall points", variable="Metrics"), height=600
            )
st.plotly_chart(fig, use_container_width=True)

#st.dataframe(df20)


"""
df3=df3[df3!=0].dropna()
df3['Points^2/Market cap points'] = df3['Points/Market cap']*df3['Overall points']
df3 = df3.sort_values(by=['Points^2/Market cap points'], ascending=False)
df3 = df3.reset_index(drop=True)
st.dataframe(df3)


import plotly.express as px
fig = px.scatter(x=df3['Overall points'], y=df3['Points^2/Market cap points'], #color="species",
                 #size=df3['Overall points'], 
                 #hover_data=df3['Ticker']
                 #mode='markers',
                 text=df3['Ticker']
                )
st.plotly_chart(fig, use_container_width=True)

collection2 = db.overall2
data2 = collection2.find()
df4 = pd.DataFrame(data2)
#df4 = df4.astype({"_id": str})
#df4 = df4.astype({" Company Name": str})
#df4 = df4.astype({" Exchange": str})
#df4 = df4.astype({" Country": str})
df4 = df4.astype(str)

df4 = df4.astype({"Overall points": float})
df4 = df4.astype({"Points/Market cap": float})

df4 = df4.drop(columns=['_id'])
df4=df4[df4!=0].dropna()
df4['Points^2/Market cap points'] = df4['Points/Market cap']*df4['Overall points']
df4 = df4.sort_values(by=['Points^2/Market cap points'], ascending=False)
df4 = df4.reset_index(drop=True)
st.dataframe(df4)

fig = px.scatter(x=df4['Overall points'], y=df4['Points^2/Market cap points'], color=df4[' Industry'],
                 #size=df3['Overall points'], 
                 #hover_data=df4['Ticker']
                 #mode='markers',
                 #text=df4['Ticker']
                )
st.plotly_chart(fig, use_container_width=True)

fig = px.scatter(x=df4['Overall points'], y=df4['Points^2/Market cap points'], color=df4[' Country'],
                 #size=df3['Overall points'], 
                 #hover_data=df4['Ticker']
                 #mode='markers',
                 #text=df4['Ticker']
                )
st.plotly_chart(fig, use_container_width=True)

fig = px.scatter(x=df4['Overall points'], y=df4['Points^2/Market cap points'], color=df4[' Sector'],
                 #size=df3['Overall points'], 
                 #hover_data=df4['Ticker']
                 #mode='markers',
                 #text=df4['Ticker']
                )
st.plotly_chart(fig, use_container_width=True)

fig = px.scatter(x=df4['Overall points'], y=df4['Points^2/Market cap points'], color=df4[' Exchange'],
                 #size=df3['Overall points'], 
                 #hover_data=df4['Ticker']
                 #mode='markers',
                 #text=df4['Ticker']
                )
st.plotly_chart(fig, use_container_width=True)

#numberofcompaniespersector = df4.groupby(' Sector').count()
#st.write(numberofcompaniespersector)

#s = df4.groupby([' Sector']).mean()
#s.sort_values(by=['Overall points'], ascending=False)

collection3 = db.overall2
data3 = collection3.find()
df5 = pd.DataFrame(data3)
marketcap = df5.astype(str)
st.dataframe(df5)
"""
