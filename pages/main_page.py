# Contents of ~/my_app/main_page.py
import streamlit as st

st.markdown("# Stonkmeizter 🎈")
st.sidebar.markdown("# Stonkomeizter 🎈")

# streamlit_app.py

import pymongo
import pandas as pd
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb+srv://niklaspee:hEjgok-wepjo5-soqcah@cluster0.80ubl.mongodb.net/?retryWrites=true&w=majority")
db = client.stonks
collection = db.overall
data = pd.DataFrame(list(collection.find()))
data
