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
industry = collection.find()
df = pd.DataFrame(industry)
df = df.drop(columns=['_id'])
df = df.astype({" Industry": str})
df = df.sort_values(by=['Overall points'], ascending=False)
#st.dataframe(df)

df20 = df.head(20)
df20 = df20.sort_values(by=['Overall points'], ascending=True)

fig = px.bar(df20, x=["Dividend points normal", "Revenues points normal", "Free Cash Flow points normal", 'Net Income points normal', 
                    'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 
                    'Payout Ratio points normal'], y=" Industry", title="Industries sorted by average overall points broken down my metric",
            labels=dict(value="Average overall points", variable="Metrics"), height=600
            )
st.plotly_chart(fig, use_container_width=True)



fig = px.scatter(df20, x="Overall points", y="Market Capitalization size", color=' Industry', log_y=True, log_x=True, text=' Industry',
                 title="Log scale of market cap by overall points",
                labels=dict(value="Average market Capitalization size", y="Average overall points"),
                 #width=800, 
                 height=900
                )

fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
st.plotly_chart(fig, use_container_width=True)


db = client.stonks
collection = db.overall2
overall = collection.find()






#@st.experimental_memo
def industrymetric(industry):
    print('running function again')
    #collection = db.overall2
    overall = collection.find({' Industry': industry })
    df = pd.DataFrame(overall)
    #df = df.drop(columns=['_id'])
    df = df.astype({" Industry": str})
    df = df[['Overall points', 'Name', 'Ticker', ' Industry','Dividend points normal', 'Revenues points normal', 'Free Cash Flow points normal', 'Net Income points normal',
     'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 'Payout Ratio points normal'
        ]]
    #dfcount = df.groupby(by=' Industry').count()
    #dfmean = df.groupby(by=' Industry').mean()
    #dfmedian = df.groupby(by=' Industry').median()
    #dfmax = df.groupby(by=' Industry').max()
    #dfmin = df.groupby(by=' Industry').min()
    #df = df.sort_values(by=['Overall points'], ascending=False)
    

    title = st.subheader(industry)
    df = df.loc[df[' Industry'] == industry]
    df = df.drop(columns=[' Industry'])


    df20 = df.head(25)
    df20 = df20.sort_values(by=['Overall points'], ascending=True)



    fig = px.bar(df20, x=["Dividend points normal", "Revenues points normal", "Free Cash Flow points normal", 'Net Income points normal', 
                        'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 
                        'Payout Ratio points normal'], y="Ticker", title="Utilities tickers sorted by average overall points broken down my metric", text='Overall points',
                labels=dict(value="Average overall points", variable="Metrics"),
                 height=600
                )



    #col1, col2, col3, col4, col5 = st.columns(5)
    #col1.metric("Number of stocks", dfcount.loc[industry][0])#, "1.2 °F")
    #col2.metric("Average score", dfmean.loc[industry][0])#, "-8%")
    #col3.metric("Median score", dfmedian.loc[industry][0])#, "4%")
    #col4.metric("Max score", dfmax.loc[industry][0])#, "4%")
    #col5.metric("Min score", dfmin.loc[industry][0])#, "4%")
    df = df.astype({"Name": str})

    st.plotly_chart(fig, use_container_width=True)
    #df = df.sort_values(by=['Overall points'], ascending=False)
    st.dataframe(df)
    return fig, col1,col2,col3,col4,col5#,df#,dfcount,dfmean,dfmedian,dfmax,dfmin

#for industry in df20[' Industry']:
#  industrymetric(industry)
#industrymetric('Asset Management')
#st.dataframe(df20)

df = pd.DataFrame(overall)
#df = df.drop(columns=['_id'])
df = df.astype({" Industry": str})
df = df[['Overall points', 'Name', 'Ticker', ' Industry','Dividend points normal', 'Revenues points normal', 'Free Cash Flow points normal', 'Net Income points normal',
 'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 'Payout Ratio points normal'
    ]]

#tickerlist = df['Ticker'].tolist()
#dfcount = df.groupby(by=' Industry').count()
#industrylist = dfcount.index.tolist()
#st.write(industrylist)

#options = st.selectbox(
#     'Pick one or several industries you want to see stats for',
#     industrylist#,
#     #industrylist[69]
#)

#st.write('You selected:', options)
#print(options)
#print(type(options))
industrymetric('Railroads')
