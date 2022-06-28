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

st.markdown("# Industry 🐝")
st.sidebar.markdown("# Industry 🐝")


def get_client():
    return MongoClient(**st.secrets["mongo"])

client = get_client()


db = client.stonks
collection = db.industrymean
data = collection.find()
df = pd.DataFrame(data)
df = df.drop(columns=['_id'])
df = df.astype({" Industry": str})
df = df.sort_values(by=['Overall points'], ascending=False)
#st.dataframe(df)

df20 = df.head(20)
#df20 = df20.sort_values(by=['Overall points'], ascending=True)

fig = px.bar(df20, x=["Dividend points normal", "Revenues points normal", "Free Cash Flow points normal", 'Net Income points normal', 
                    'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 
                    'Payout Ratio points normal'], y=" Industry", title="Industries sorted by average overall points broken down my metric",
            labels=dict(value="Average overall points", variable="Metrics")
            )
st.plotly_chart(fig, use_container_width=True)



fig = px.scatter(df20, x="Overall points", y="Market Capitalization size", color=' Industry', log_y=True, text=' Industry',
                 title="Log scale of market cap by overall points",
                labels=dict(value="Average market Capitalization size", y="Average overall points"),
                 #width=800, 
                 height=800
                )

fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
st.plotly_chart(fig, use_container_width=True)








def industrymetric(industry):
    db = client.stonks
    collection = db.overall2
    data = collection.find()
    df = pd.DataFrame(data)
    df = df.drop(columns=['_id'])
    df = df.astype({" Industry": str})
    dfcount = df.groupby(by=' Industry').count()
    dfmean = df.groupby(by=' Industry').mean()
    dfmedian = df.groupby(by=' Industry').median()
    dfmax = df.groupby(by=' Industry').max()
    dfmin = df.groupby(by=' Industry').min()
    #df = df.astype({"Name": str})
    df = df.sort_values(by=['Overall points'], ascending=False)
    df = df[['Overall points', 'Name', 'Ticker', ' Industry','Dividend points normal', 'Revenues points normal', 'Free Cash Flow points normal', 'Net Income points normal',
         'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 'Payout Ratio points normal'
            ]]
    title = st.subheader(industry)
    df = df.loc[df[' Industry'] == industry]
    df = df.drop(columns=[' Industry'])


    df20 = df.head(20)
    df20 = df20.sort_values(by=['Overall points'], ascending=True)



    fig = px.bar(df20, x=["Dividend points normal", "Revenues points normal", "Free Cash Flow points normal", 'Net Income points normal', 
                        'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 
                        'Payout Ratio points normal'], y="Ticker", title="Utilities tickers sorted by average overall points broken down my metric", text='Overall points',
                labels=dict(value="Average overall points", variable="Metrics"),
                 height=500
                )



    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Number of stocks", dfcount.loc[industry][0])#, "1.2 °F")
    col2.metric("Average score", dfmean.loc[industry][0])#, "-8%")
    col3.metric("Median score", dfmedian.loc[industry][0])#, "4%")
    col4.metric("Max score", dfmax.loc[industry][0])#, "4%")
    col5.metric("Min score", dfmin.loc[industry][0])#, "4%")
    df = df.astype({"Name": str})

    st.plotly_chart(fig, use_container_width=True)
    #df = df.sort_values(by=['Overall points'], ascending=False)
    st.dataframe(df)
    return fig, col1,col2,col3,col4#,col5,df,dfcount,dfmean,dfmedian,dfmax,dfmin

#for industry in df[' Industry']:
#  industrymetric(industry)
industrymetric('Asset Management')
st.write(dfcount)
#st.dataframe(dfmean)
#st.dataframe(dfmedian)
#st.dataframe(dfmax)
#st.dataframe(dfmin)
