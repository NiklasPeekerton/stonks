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
    df = df[['Overall points', 'Name', 'Ticker', ' Industry',' Sector', 'Market Capitalization size','Dividend points normal', 'Revenues points normal', 'Free Cash Flow points normal', 'Net Income points normal',
     'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 'Payout Ratio points normal'
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
                        'Payout Ratio points normal'], y="Name", title="Tickers sorted by average overall points broken down my metric", text='Overall points',
                labels=dict(value="Average overall points", variable="Metrics"),
                 height=600
                )

st.plotly_chart(fig, use_container_width=True)
st.dataframe(full)
