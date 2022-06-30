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

st.markdown("# Sectors 🐚")
st.sidebar.markdown("# Sectors 🐚")


def get_client():
    return MongoClient(**st.secrets["mongo"])

client = get_client()


db = client.stonks
collection = db.sectorsmean
sector = collection.find()
df = pd.DataFrame(sector)
df = df.drop(columns=['_id'])
df = df.astype({" Sector": str})
df = df.sort_values(by=['Overall points'], ascending=False)
#st.dataframe(df)

df20 = df.head(20)
df20 = df20.sort_values(by=['Overall points'], ascending=True)

fig = px.bar(df20, x=["Dividend points normal", "Revenues points normal", "Free Cash Flow points normal", 'Net Income points normal', 
                    'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 
                    'Payout Ratio points normal'], y=" Sector", title="Industries sorted by average overall points broken down my metric",
            labels=dict(value="Average overall points", variable="Metrics"), height=600
            )
st.plotly_chart(fig, use_container_width=True)



fig = px.scatter(df20, x="Overall points", y="Market Capitalization size", color=' Sector', log_y=True, log_x=True, text=' Sector',
                 title="Log scale of market cap by overall points",
                labels=dict(value="Average market Capitalization size", y="Average overall points"),
                 #width=800, 
                 height=900
                )

fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
st.plotly_chart(fig, use_container_width=True)







@st.experimental_memo
def sectormetric(sector):
    collection = db.overall2
    overall = collection.find({' Sector': sector })
    df = pd.DataFrame(overall)
    df = df.astype({" Sector": str})
    df = df[['Overall points', 'Market Capitalization size','Name', 'Ticker', ' Sector', 'Dividend points normal', 'Revenues points normal', 'Free Cash Flow points normal', 'Net Income points normal',
     'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 'Payout Ratio points normal'
        ]]

    df = df.loc[df[' Sector'] == sector]
    df = df.drop(columns=[' Sector'])


    df20 = df.head(25)
    df20 = df20.sort_values(by=['Overall points'], ascending=True)

    df = df.astype({"Name": str})

    return df, df20



sectorlist = df[' Sector'].tolist()

options = st.selectbox(
     'Pick a sector you want to see stats for',
     sectorlist#,
#     #sectorlist[69]
)

st.subheader(options)

full = sectormetric(options)[0]
top20 = sectormetric(options)[1]

fig = px.bar(top20, x=["Dividend points normal", "Revenues points normal", "Free Cash Flow points normal", 'Net Income points normal', 
                        'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 
                        'Payout Ratio points normal'], y="Ticker", title=options+" tickers sorted by average overall points broken down my metric", text='Overall points',
                labels=dict(value="Average overall points", variable="Metrics"),
                 height=600
                )


test = full.describe()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Number of stocks", test.loc['count'][0])
col2.metric("Average score", test.loc['mean'][0])
col3.metric("Min score", test.loc['min'][0])
col4.metric("Max score", test.loc['max'][0])

col5, col6, col7 = st.columns(3)
col5.metric("25% score", test.loc['25%'][0])
col6.metric("50% score", test.loc['50%'][0])
col7.metric("75% score", test.loc['75%'][0])
    
st.plotly_chart(fig, use_container_width=True)
test = full.style.format({"Market Capitalization size": "${:20,.0f}"})\
                 .hide_index()\
                 .bar(subset=["Market Capitalization size",], color='lightgreen')\
                 .bar(subset=["Revenues points normal"], color='#ee1f5f')\
                 .bar(subset=["Dividend points normal"], color='#FFA07A')\
                 .bar(subset=["Free Cash Flow points normal"], color='#FFA07A')\
                 .bar(subset=["Net Income points normal"], color='#FFA07A')\
                 .bar(subset=["Current Ratio points normal"], color='#FFA07A')\
                 .bar(subset=["Weighted Average Shares (Diluted) points normal"], color='#FFA07A')\
                 .bar(subset=["Payout Ratio points normal"], color='#FFA07A')
                     
#st.table(test)
st._legacy_dataframe(test)
#st.markdown(
#    test_styled.to_html(table_uuid="table_1"), unsafe_allow_html=True
#)
