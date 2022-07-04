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


st.markdown("# Score breakdown 🚬")
st.sidebar.markdown("# Score breakdown 🚬")


def get_client():
    return MongoClient(**st.secrets["mongo"])

client = get_client()
db = client.stonks
collection_name = ['ncav','enterprisevalue']

options = st.selectbox(
     'Pick a metric you want to see score breakdown for',
     collection_name#,
#     #industrylist[69]
)



@st.experimental_memo
def metrics():
    mycol = db[options]
    industry = mycol.find()
    df = pd.DataFrame(industry)
    df = df.drop(columns=['_id'])
    #df = df.astype({" Industry": str})
    #logdf = df.sort_values(by=['Market Capitalization size'], ascending=False)
    #logdf = logdf[:-6]
    #df = df.sort_values(by=['Overall points'], ascending=False)
    #st.dataframe(df)

    df20 = df.head(20)
    #df20 = df20.sort_values(by=['Enterprise Valuation points'], ascending=True)
    return df, df20

allmetric = metrics()[0]
topmetric = metrics()[1]

#fig = px.bar(topmetric, x=["Enterprise Valuation p3 points", 
#                           "Enterprise Valuation slope points", 
#                           "Enterprise Valuation growth points", 
#                           'Enterprise Valuation endvaluediff points', 
#                           'Enterprise Valuation count_pos points', 
#                           'Enterprise Valuation size points', 
#                           'Enterprise Valuation povsneg points', 
#                           'Enterprise Valuation relative_sum_neg points',
#                           'Enterprise Valuation relative_sum_pos points'], 
#                           y="Ticker", title="Tickers sorted by Enterprise Valuation points broken down my metric", text='Enterprise Valuation points',
#                          labels=dict(value="Enterprise Valuation points", variable="Metrics"),
#                          height=600
 #               )

#st.plotly_chart(fig, use_container_width=True)
st.write(allmetric)
