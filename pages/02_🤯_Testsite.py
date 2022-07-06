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
    collection = db.overall3
    overall = collection.find()
    df = pd.DataFrame(overall)
    df = df.drop(columns=['_id'])
    df = df.drop(columns=[' CUSIP'])
    df = df.drop(columns=['   CIK'])
    df = df.astype({" IPO Date": str})
    #df = df.astype({" Industry": str})
    df = df[['Market cap','Name', 'Ticker', 'Dividend points normal', 'Revenues points normal', 'Free Cash Flow points normal', 'Net Income points normal',
             'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 'Payout Ratio points normal',
             'Debt to Equity Ratio points normal', 'Enterprise Valuation points normal', 'Total Assets points normal', 'Total Liabilities points normal', 'Book Value Per Share points normal',
             'Price To Book Value points normal', 'Price To Earnings Ratio points normal', 'Total ratio points normal', 'Dividend Yield points normal', 'Market Capitalization size'
        ]]

    #df = df.loc[df[' Industry'] == industry]
    #df = df.drop(columns=[' Industry'])


    df25 = df.head(25)
    #df25 = df25.sort_values(by=['Overall points'], ascending=True)

    df = df.astype({"Name": str})

    return df, df25

full = givestonks()[0]
top25 = givestonks()[1]



#collection = db.overall2
#data = collection.find()
#data1 = (data.index += 1 )

#df = pd.DataFrame(data)
#df = df.drop(columns=['_id'])
#df = df.drop(columns=[' CUSIP'])
#df = df.drop(columns=['   CIK'])
#df = df.astype({" IPO Date": str})

col1, col2, col3, col4 = st.columns(4)
#weightrev = st.slider('Weight for Revenue', 0.0, 10.0, 1.0)
col1.slider('Weight for Revenue', 0.0, 10.0, 1.0)
col2.slider('Weight for Dividends', 0.0, 10.0, 1.0)
col3.slider('Weight for FCF', 0.0, 10.0, 1.0)
col4.slider('Weight for Net Income', 0.0, 10.0, 1.0)

#weightdiv = st.slider('Weight for Dividends', 0.0, 10.0, 1.0)
#weightfcf = st.slider('Weight for FCF', 0.0, 10.0, 1.0)
#weightni = st.slider('Weight for Net Income', 0.0, 10.0, 1.0)
weightnim = st.slider('Weight for Net Income Margin', 0.0, 10.0, 1.0)
weightcr = st.slider('Weight for Current Ratio', 0.0, 10.0, 1.0)
weightos = st.slider('Weight for Outstanding shares', 0.0, 10.0, 1.0)
weightpr = st.slider('Weight for Payout Ratio', 0.0, 10.0, 1.0)

full['Revenues points normal'] = full['Revenues points normal']*weightrev
full['Dividend points normal'] = full['Dividend points normal']*weightdiv
full['Free Cash Flow points normal'] = full['Free Cash Flow points normal']*weightfcf
full['Net Income points normal'] = full['Net Income points normal']*weightni
full['Net Income Margin points normal'] = full['Net Income Margin points normal']*weightnim
full['Current Ratio points normal'] = full['Current Ratio points normal']*weightcr
full['Weighted Average Shares (Diluted) points normal'] = full['Weighted Average Shares (Diluted) points normal']*weightos
full['Payout Ratio points normal'] = full['Payout Ratio points normal']*weightpr

#full['Overall points'] = full['Overall points']+(full['Revenues points normal']-(full['Revenues points normal']/weightrev)) + (full['Dividend points normal']-(full['Dividend points normal']/weightdiv)) + (full['Free Cash Flow points normal']-(full['Free Cash Flow points normal']/weightfcf)) + (full['Net Income points normal']-(full['Net Income points normal']/weightni)) + (full['Net Income Margin points normal']-(full['Net Income Margin points normal']/weightnim)) + (full['Current Ratio points normal']-(full['Current Ratio points normal']/weightcr)) + (full['Weighted Average Shares (Diluted) points normal']-(full['Weighted Average Shares (Diluted) points normal']/weightos)) + (full['Payout Ratio points normal']-(full['Payout Ratio points normal']/weightpr))
full['Overall points'] = full['Revenues points normal']*weightrev + full['Dividend points normal']*weightdiv + full['Free Cash Flow points normal']*weightfcf + full['Net Income points normal']*weightni + full['Net Income Margin points normal']*weightnim + full['Current Ratio points normal']*weightcr + full['Weighted Average Shares (Diluted) points normal']*weightos + full['Payout Ratio points normal']*weightpr

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

styledf = full.style.format({"Market Capitalization size": '${:20,.0f}', "Overall points": "🏆{:20,.0f}"
                         , "Dividend points normal": "🏆{:20,.0f}", "Revenues points normal": "🏆{:20,.0f}"
                         , "Free Cash Flow points normal": "🏆{:20,.0f}", "Net Income points normal": "🏆{:20,.0f}"
                         , "Net Income Margin points normal": "🏆{:20,.0f}", "Current Ratio points normal": "🏆{:20,.0f}"
                         , "Weighted Average Shares (Diluted) points normal": "🏆{:20,.0f}", "Payout Ratio points normal": "🏆{:20,.0f}"#,
                          #'Website': make_clickable
                         
                         }, hyperlinks='html')\
                 .hide_index()\
                 .bar(subset=["Overall points"], color='1B2432')\
                 .bar(subset=["Market Capitalization size"], color='lightgreen')\
                 .bar(subset=["Revenues points normal"], color='#EF553B')\
                 .bar(subset=["Dividend points normal"], color='#646FFB')\
                 .bar(subset=["Free Cash Flow points normal"], color='#00CC96')\
                 .bar(subset=["Net Income points normal"], color='#AB63FA')\
                 .bar(subset=["Net Income Margin points normal"], color='#FFA15A')\
                 .bar(subset=["Current Ratio points normal"], color='#19D3F3')\
                 .bar(subset=["Weighted Average Shares (Diluted) points normal"], color='#FF6692')\
                 .bar(subset=["Payout Ratio points normal"], color='#B6E980')

                 #.background_gradient(cmap='Blues')
                     
#test1 =  test.style.format({'Name': make_clickable_both}).bar(subset=['Overall points'], align='mid', color=['#d65f5f', '#5fba7d'])
#st.table(test)
st._legacy_dataframe(styledf, height=800)
