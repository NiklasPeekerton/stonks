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
#st.dataframe(dftrim)
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

dfcount = df.groupby(by=' Sector').count()
dfmean = df.groupby(by=' Sector').mean()
dfmedian = df.groupby(by=' Sector').median()
dfmax = df.groupby(by=' Sector').max()
dfmin = df.groupby(by=' Sector').min()
df = df.astype({"Name": str})
dfutil = df.loc[df[' Sector'] == 'Utilities']
dfutil = dfutil.drop(columns=[' Sector'])


df20 = df.head(20)
df20 = df20.sort_values(by=['Overall points'], ascending=True)



fig = px.bar(df20, x=["Dividend points normal", "Revenues points normal", "Free Cash Flow points normal", 'Net Income points normal', 
                    'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 
                    'Payout Ratio points normal'], y="Ticker", title="Utilities tickers sorted by average overall points broken down my metric", text='Overall points',
            labels=dict(value="Average overall points", variable="Metrics"),
             height=500
            )

st.subheader("Utilities")

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Number of stocks", dfcount.loc['Utilities'][0])#, "1.2 °F")
col2.metric("Average score", dfmean.loc['Utilities'][0])#, "-8%")
col3.metric("Median score", dfmedian.loc['Utilities'][0])#, "4%")
col4.metric("Max score", dfmax.loc['Utilities'][0])#, "4%")
col5.metric("Min score", dfmin.loc['Utilities'][0])#, "4%")

st.plotly_chart(fig, use_container_width=True)
#df = df.sort_values(by=['Overall points'], ascending=False)
st.dataframe(df)
#dfg = df.index.describe()


#st.image('https://i.redd.it/fxrb1fsftv391.jpg')

st.subheader("Consumer defensive")
df = df.loc[df[' Sector'] == 'Consumer Defensive']
df = df.drop(columns=[' Sector'])


df20 = df.head(20)
df20 = df20.sort_values(by=['Overall points'], ascending=True)



fig = px.bar(df20, x=["Dividend points normal", "Revenues points normal", "Free Cash Flow points normal", 'Net Income points normal', 
                    'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 
                    'Payout Ratio points normal'], y="Ticker", title="Utilities tickers sorted by average overall points broken down my metric", text='Overall points',
            labels=dict(value="Average overall points", variable="Metrics"),
             height=500
            )



col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Number of stocks", dfcount.loc['Consumer Defensive'][0])#, "1.2 °F")
col2.metric("Average score", dfmean.loc['Consumer Defensive'][0])#, "-8%")
col3.metric("Median score", dfmedian.loc['Consumer Defensive'][0])#, "4%")
col4.metric("Max score", dfmax.loc['Consumer Defensive'][0])#, "4%")
col5.metric("Min score", dfmin.loc['Consumer Defensive'][0])#, "4%")

st.plotly_chart(fig, use_container_width=True)
#df = df.sort_values(by=['Overall points'], ascending=False)
st.dataframe(df)




def sectormetric(sector):
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
    title = st.subheader(sector)
    df = df.loc[df[' Sector'] == sector]
    df = df.drop(columns=[' Sector'])


    df20 = df.head(20)
    df20 = df20.sort_values(by=['Overall points'], ascending=True)



    fig = px.bar(df20, x=["Dividend points normal", "Revenues points normal", "Free Cash Flow points normal", 'Net Income points normal', 
                        'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 
                        'Payout Ratio points normal'], y="Ticker", title="Utilities tickers sorted by average overall points broken down my metric", text='Overall points',
                labels=dict(value="Average overall points", variable="Metrics"),
                 height=500
                )



    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Number of stocks", dfcount.loc[sector][0])#, "1.2 °F")
    col2.metric("Average score", dfmean.loc[sector][0])#, "-8%")
    col3.metric("Median score", dfmedian.loc[sector][0])#, "4%")
    col4.metric("Max score", dfmax.loc[sector][0])#, "4%")
    col5.metric("Min score", dfmin.loc[sector][0])#, "4%")

    st.plotly_chart(fig, use_container_width=True)
    #df = df.sort_values(by=['Overall points'], ascending=False)
    st.dataframe(df)
    return fig, col1,col2,col3,col4,col5,df

sectormetric('Consumer Defensive')
