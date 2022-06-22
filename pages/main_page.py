# Contents of ~/my_app/main_page.py
import streamlit as st
import pandas as pd
import pymongo
#import pymongo[srv]
from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np
import altair as alt

st.markdown("# Stonkomeizter 🚀🚀🚀")
st.sidebar.markdown("# Stonkomeizter 🚀🚀🚀")

# streamlit_app.py

#@st.cache()#hash_funcs={MongoClient: id}
def get_client():
    return MongoClient(**st.secrets["mongo"])

client = get_client()


db = client.stonks
collection = db.overall
data = collection.find()
#data1 = (data.index += 1 )

df = pd.DataFrame(data)
df = df.astype({"_id": str})
df1 = df.drop(columns=['_id'])
#st.dataframe(df1, width=1500, height=None)
test = df1.astype(str)

st.subheader("'Old' scores", anchor=None)
st.dataframe(test)
test1 = test[:500]


collection1 = db.overall1
data1 = collection1.find()


df2 = pd.DataFrame(data1)

df3 = df2.astype({"_id": str})
df3 = df2.drop(columns=['_id'])
#st.dataframe(df1, width=1500, height=None)
#test = df2.astype(str)

st.subheader("'New' scores", anchor=None)
df3=df3[df3!=0].dropna()
st.dataframe(df3)
#test1 = test[:500]

#st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)

#st.bar_chart(test1[['Ticker','Overall points']])

#c = alt.Chart(test1).mark_bar().encode(
#    alt.X('Overall points:Q'),
#    alt.Y('Ticker:O', sort='-x'))
#st.altair_chart(c, use_container_width=True)

#source = data.barley()

#alt.Chart(source).mark_bar().encode(
#    x='sum(yield)',
#    y='variety',
#    color='site'
#)


st.subheader("Testsection 🚀💩🔞🚭☠︎🤯💥")

weight = st.slider('Weight for Revenue', 1, 10, 1)

df3['Revenues points normal'] = df3['Revenues points normal']*weight

df3['Overall points'] = df3['Overall points'] + (df3['Revenues points normal']-(df3['Revenues points normal']/weight))

df3 = df3.sort_values(by=['Overall points'], ascending=False)
df3 = df3.reset_index(drop=True)

#df3['Overall points2'] = df3['Revenues points normal'] + df3['Dividend points normal'] 
#+ df3['Free Cash Flow points normal'] + df3['Net Income points normal'] + df3['Net Income Margin points normal'] + df3['Current Ratio points normal']
#+ df3['Weighted Average Shares (Diluted) points normal'] + df3['Payout Ratio points normal']

st.dataframe(df3)



df3=df3[df3!=0].dropna()
df3['Points^2/Market cap points'] = df3['Points/Market cap']*df3['Overall points']
df3 = df3.sort_values(by=['Points^2/Market cap points'], ascending=False)
df3 = df3.reset_index(drop=True)
st.dataframe(df3)


import plotly.express as px
fig = px.scatter(x=df3['Overall points'], y=df3['Points^2/Market cap points'], #color="species",
                 #size=df3['Overall points'], 
                 #hover_data=df3['Ticker']
                 #mode='markers',
                 text=df3['Ticker']
                )
st.plotly_chart(fig, use_container_width=True)

collection2 = db.overall2
data2 = collection2.find()
df4 = pd.DataFrame(data2)
#df4 = df4.astype({"_id": str})
#df4 = df4.astype({" Company Name": str})
#df4 = df4.astype({" Exchange": str})
#df4 = df4.astype({" Country": str})
df4 = df4.astype(str)
df4 = df4.drop(columns=['_id'])
df4=df4[df4!=0].dropna()
df4['Points^2/Market cap points'] = df4['Points/Market cap']*df4['Overall points']
df4 = df4.sort_values(by=['Points^2/Market cap points'], ascending=False)
df4 = df4.reset_index(drop=True)
st.dataframe(df4)

fig = px.scatter(x=df4['Overall points'], y=df4['Points^2/Market cap points'], color=" Industry",
                 #size=df3['Overall points'], 
                 #hover_data=df3['Ticker']
                 #mode='markers',
                 #text=df4['Ticker']
                )
st.plotly_chart(fig, use_container_width=True)
