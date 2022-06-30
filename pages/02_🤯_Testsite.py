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

st.markdown("# Stonkolawdhavemercy 🚀💩🔞🚭☠︎🤯💥")
st.sidebar.markdown("# Testsite 🚀💩🔞🚭☠︎🤯💥")

# streamlit_app.py

#@st.cache(hash_funcs={MongoClient: id})
def get_client():
    return MongoClient(**st.secrets["mongo"])

client = get_client()


db = client.stonks
collection = db.overall2
data = collection.find()
#data1 = (data.index += 1 )

df = pd.DataFrame(data)


weight = st.slider('Weight for Revenue', 1, 10, 1)

df['Revenues points normal'] = df['Revenues points normal']*weight

df['Overall points'] = df['Overall points'] + (df['Revenues points normal']-(df['Revenues points normal']/weight))

df = df.sort_values(by=['Overall points'], ascending=False)
df = df.reset_index(drop=True)

#df3['Overall points2'] = df3['Revenues points normal'] + df3['Dividend points normal'] 
#+ df3['Free Cash Flow points normal'] + df3['Net Income points normal'] + df3['Net Income Margin points normal'] + df3['Current Ratio points normal']
#+ df3['Weighted Average Shares (Diluted) points normal'] + df3['Payout Ratio points normal']

df20 = df.head(20)
df20 = df20.sort_values(by=['Overall points'], ascending=True)

fig = px.bar(df20, x=["Dividend points normal", "Revenues points normal", "Free Cash Flow points normal", 'Net Income points normal', 
                    'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 
                    'Payout Ratio points normal'], y=" Industry", title="Industries sorted by average overall points broken down my metric",
            labels=dict(value="Average overall points", variable="Metrics"), height=600
            )
st.plotly_chart(fig, use_container_width=True)

st.dataframe(df20)



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

