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

plost.bar_chart(
    data=df,
    bar=' Sector',
    value='Overall points',
    direction='horizontal')

plost.scatter_chart(
    data=df,
    x='Market Capitalization size',
    y='Overall points',
    #size='c',
    #opacity='b',
    height=500)
#data = data1.astype(str)

#st.dataframe(df1, width=1500, height=None)
#test = df2.astype(str)


st.subheader("blö", anchor=None)

#s = data.groupby([' Sector']).mean()
#mean = s.sort_values(by=['Overall points'], ascending=False)



