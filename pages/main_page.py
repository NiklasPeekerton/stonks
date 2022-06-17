# Contents of ~/my_app/main_page.py
import streamlit as st
import pandas as pd
import pymongo
#import pymongo[srv]
from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np

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
st.dataframe(df1, width=1500, height=None)

st.pyplot(df1[:100])
