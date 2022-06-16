# Contents of ~/my_app/main_page.py
import streamlit as st
import pandas as pd
import pymongo
from pymongo import MongoClient

st.markdown("# Stonkmeizter 🎈")
st.sidebar.markdown("# Stonkomeizter 🎈")

# streamlit_app.py


# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

#client = init_connection()

my_db.connect(**st.secrets.mongo)

@st.cache(hash_funcs={MongoClient: id})
def get_client():
    return MongoClient(**st.secrets["mongo"]['host'])

client = get_client()
db = client.stonks
collection = db.overall

st.write(collection.find()[0])

#print(client)

db = client.stonks
st.markdown(db)
collection = db.overall
st.markdown(collection)

items = db.overall.find()
items = list(items)
#items

#data = pd.DataFrame(list(collection.find()))
#st.data

#st.write("DB username:", st.secrets["mongo"]["host"])
#st.write("DB password:", st.secrets["mongo"]["password"])
