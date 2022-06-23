# Contents of ~/my_app/main_page.py
import streamlit as st
import pandas as pd
import pymongo
#import pymongo[srv]
from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import plost
import plotly.express as px

st.set_page_config(layout="wide")

st.markdown("# Segmentazione 💩")
st.sidebar.markdown("# Segment 💩")


def get_client():
    return MongoClient(**st.secrets["mongo"])

client = get_client()


db = client.stonks
collection = db.sectorsmean
data = collection.find()
df = pd.DataFrame(data)
df = df.drop(columns=['_id'])
df = df.astype({" Sector": str})
df = df.sort_values(by=['Overall points'], ascending=True)
#st.dataframe(df)

fig = px.bar(df, x=["Dividend points normal", "Revenues points normal", "Free Cash Flow points normal", 'Net Income points normal', 
                    'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 
                    'Payout Ratio points normal'], y=" Sector", title="Sectors sorted by average overall points broken down my metric",
            labels=dict(value="Average overall points", variable="Metrics")
            )
st.plotly_chart(fig, use_container_width=True)

dftrim = df.drop([17,5])

fig = px.scatter(df, x="Overall points", y="Market Capitalization size", color=' Sector', log_y=True, text=' Sector',
                 title="Log scale of market cap by overall points",
                labels=dict(value="Average market Capitalization size", y="Average overall points"),
                 #width=800, 
                 height=800
                )

fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
st.plotly_chart(fig, use_container_width=True)

#gapminder_2002 = gapminder[gapminder['year']==2002]
#dftrim = dftrim.set_index(' Sector')
dftrim = dftrim[['Overall points', ' Sector','Dividend points normal', 'Revenues points normal', 'Free Cash Flow points normal', 'Net Income points normal',
     'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 'Payout Ratio points normal']]
st.dataframe(dftrim)
#st.bar_chart(dftrim)


db = client.stonks
collection = db.overall2
data = collection.find()
df = pd.DataFrame(data)
df = df.drop(columns=['_id'])
df = df.astype({" Sector": str})
df = df.sort_values(by=['Overall points'], ascending=False)
df = df[['Overall points', 'Name', 'Ticker', ' Sector','Dividend points normal', 'Revenues points normal', 'Free Cash Flow points normal', 'Net Income points normal',
     'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 'Payout Ratio points normal'
        ]]

df = df.astype({"Name": str})
df = df.loc[df[' Sector'] == 'Utilities']
df = df.drop(columns=[' Sector'])
st.dataframe(df)

df = df.sort_values(by=['Overall points'], ascending=False)
df = df.head(20)
fig = px.bar(df, x=["Dividend points normal", "Revenues points normal", "Free Cash Flow points normal", 'Net Income points normal', 
                    'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 
                    'Payout Ratio points normal'], y="Ticker", title="Utilities tickers sorted by average overall points broken down my metric",
            labels=dict(value="Average overall points", variable="Metrics"),
             height=700
            )
st.plotly_chart(fig, use_container_width=True)



st.image('https://i.redd.it/fxrb1fsftv391.jpg')
