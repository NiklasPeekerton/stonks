# Contents of ~/my_app/main_page.py
import streamlit as st
import pandas as pd
import pymongo
#import pymongo[srv]
from pymongo import MongoClient

st.markdown("# Stonkmeizter 🎈")
st.sidebar.markdown("# Stonkomeizter 🎈")

# streamlit_app.py

@st.cache(hash_funcs={MongoClient: id})
def get_client():
    return MongoClient(**st.secrets["mongo"])

client = get_client()


db = client.stonks
collection = db.overall
data = collection.find()
data1 = data.index += 1 

df = pd.DataFrame(data1)
df = df.astype({"_id": str})
df1 = df.drop(columns=['_id'])
st.dataframe(df1)

