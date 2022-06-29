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

#Sorted by value
collection1 = db.overall1
data1 = collection1.find()
df2 = pd.DataFrame(data1)
df3 = df2.astype({"_id": str})
df3 = df2.drop(columns=['_id'])

st.subheader("Sorted by value 💰", anchor=None)
df3=df3[df3!=0].dropna()
points = df3['Points/Market cap']*df3['Overall points']

df3.insert(3, "Value points", points)
df3 = df3.sort_values(by=['Value points'], ascending=False)
df3 = df3.reset_index(drop=True)
st.dataframe(df3)


collection = db.overall
data = collection.find()


df = pd.DataFrame(data)
df = df.astype({"_id": str})
df1 = df.drop(columns=['_id'])
#st.dataframe(df1, width=1500, height=None)
test = df1.astype(str)

#st.subheader("'New' scores", anchor=None)
#df4 = pd.DataFrame(data1)
#df5 = df4.astype({"_id": str})
#df5 = df4.drop(columns=['_id'])

#df4=df4[df4!=0].dropna()
#st.dataframe(df4)

st.subheader("'Old' scores", anchor=None)
st.dataframe(test)
test1 = test[:500]


collection1 = db.overall1
data1 = collection1.find()
df2 = pd.DataFrame(data1)

df3 = df2.astype({"_id": str})
df3 = df2.drop(columns=['_id'])






@st.experimental_memo
def giveme(coll):
    collection = db.coll
    overall = collection.find()
    df = pd.DataFrame(overall)
    df = df.astype({" Industry": str})
    df = df[['Overall points', 'Name', 'Ticker', ' Industry',' Sector', 'Dividend points normal', 'Revenues points normal', 'Free Cash Flow points normal', 'Net Income points normal',
     'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 'Payout Ratio points normal'
        ]]



    df20 = df.head(25)
    df20 = df20.sort_values(by=['Overall points'], ascending=True)

    df = df.astype({"Name": str})

    return df, df20


giveme(df20)
