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
#st.sidebar.markdown("# Stonkomeizter 🚀🚀🚀")

# streamlit_app.py

@st.cache(hash_funcs={MongoClient: id})
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
st.dataframe(test)
test1 = test[:500]

#st.bar_chart(test1[['Ticker','Overall points']])

c = alt.Chart(test1).mark_bar().encode(
    alt.X('Overall points:Q'),
    alt.Y('Ticker:O', sort='-x'))
st.altair_chart(c, use_container_width=True)
