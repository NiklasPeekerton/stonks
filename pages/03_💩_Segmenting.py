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
df = df.sort_values(by=['Overall points'], ascending=True)
st.dataframe(df)

fig = px.bar(df, x=["Dividend points normal", "Revenues points normal", "Free Cash Flow points normal", 'Net Income points normal', 
                    'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 
                    'Payout Ratio points normal'], y=" Sector", title="Sectors sorted by average overall points broken down my metric",
            labels=dict(value="Average overall points", variable="Metrics")
            )
st.plotly_chart(fig, use_container_width=True)

dftrim = df.drop([17,5])

fig = px.scatter(df, x="Market Capitalization size", y="Overall points", color=' Sector', log_x=True,
                 title="Log scale of market cap by overall points",
                labels=dict(value="Average market Capitalization size", y="Average overall points")
                )
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
df = df[['Overall points', ' Sector','Dividend points normal', 'Revenues points normal', 'Free Cash Flow points normal', 'Net Income points normal',
     'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 'Payout Ratio points normal'
        ]]
st.dataframe(df)




#wide_df = px.data.medals_wide()

fig = px.bar(df, x=["Dividend points normal", "Revenues points normal", "Free Cash Flow points normal", 'Net Income points normal', 'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 'Payout Ratio points normal'], y=" Sector", title="Wide-Form Input")
st.plotly_chart(fig, use_container_width=True)

sector = alt.Chart(dftrim).mark_bar().encode(
    x='Overall points:Q',
    #y=alt.Y(' Sector:N', sort='-x'),
    y='sum(Overall points)',
    #color=['Dividend points normal', 'Revenues points normal'],
    order=alt.Order(
      # Sort the segments of the bars by this field
      ' Sector',
      sort='ascending'
    )
).properties(height=700)

st.altair_chart(sector)
