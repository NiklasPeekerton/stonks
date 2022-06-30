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

st.markdown("# Stonkomeizter 🚀🚀🚀")
st.sidebar.markdown("# Stonkomeizter 🚀🚀🚀")

# streamlit_app.py

#@st.cache()#hash_funcs={MongoClient: id}
def get_client():
    return MongoClient(**st.secrets["mongo"])





@st.experimental_memo
def giveme():
    client = get_client()
    db = client.stonks
    collection = db.overall2
    overall = collection.find()
    df = pd.DataFrame(overall)
    df = df[['Overall points', 'Market Capitalization size','Name', 'Ticker', ' Sector', ' Industry','Dividend points normal', 'Revenues points normal', 'Free Cash Flow points normal', 'Net Income points normal',
     'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 'Payout Ratio points normal'#, 'Website'
        ]]



    df25 = df.head(25)
    df25 = df25.sort_values(by=['Overall points'], ascending=True)

    df = df.astype({"Name": str})
    df = df.astype({" Industry": str})
    df = df.astype({" Sector": str})

    return df, df25


#giveme(overall2)

full = giveme()[0]
top25 = giveme()[1]

fig = px.bar(top25, x=["Dividend points normal", "Revenues points normal", "Free Cash Flow points normal", 'Net Income points normal', 
                        'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 
                        'Payout Ratio points normal'], y="Ticker", title="Tickers sorted by average overall points broken down my metric", text='Overall points',
                labels=dict(value="Average overall points", variable="Metrics"),
                 height=600,
                hover_name="Name"
                )

test = full.style.format({"Market Capitalization size": '${0:,.2f}', "Overall points": "🏆{:20,.0f}"
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

st.plotly_chart(fig, use_container_width=True)
st._legacy_dataframe(test)
