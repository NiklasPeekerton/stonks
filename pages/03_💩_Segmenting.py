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

st.markdown("# Segmentazione 💩")
st.sidebar.markdown("# Segment 💩")
st.image('https://i.redd.it/fxrb1fsftv391.jpg')

def get_client():
    return MongoClient(**st.secrets["mongo"])

client = get_client()


db = client.stonks
collection = db.sectorsmean
data = collection.find()
df = pd.DataFrame(data)
df = df.drop(columns=['_id'])
df = df.astype({" Sector": str})
df = df.sort_values(by=['Overall points'], ascending=False)
st.dataframe(df)

dftrim = df.drop([17,5])

plost.bar_chart(
    data=dftrim,
    bar=' Sector',
    value=['Dividend points normal', 'Revenues points normal', 'Free Cash Flow points normal', 'Net Income points normal',
     'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 'Payout Ratio points normal'],
    direction='horizontal')

plost.bar_chart(
    data=dftrim,
    bar=' Sector',
    value='Market Capitalization size',
    direction='horizontal')

plost.scatter_chart(
    data=dftrim,
    x='Overall points',
    y='Market Capitalization size',
    size='Overall points',
    #opacity='b',
    height=500)

#gapminder_2002 = gapminder[gapminder['year']==2002]
#dftrim = dftrim.set_index(' Sector')
dftrim = dftrim[[' Sector','Dividend points normal', 'Revenues points normal', 'Free Cash Flow points normal', 'Net Income points normal',
     'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 'Payout Ratio points normal']]
st.dataframe(dftrim)
#st.bar_chart(dftrim)

sector = alt.Chart(dftrim).mark_bar().encode(
    x=' Sector:Q',
    y='Overall points:O',
    #color=['Dividend points normal', 'Revenues points normal'],
    order=alt.Order(
      # Sort the segments of the bars by this field
      'Dividend points normal',
      sort='ascending'
    )
)

st.altair_chart(sector)
