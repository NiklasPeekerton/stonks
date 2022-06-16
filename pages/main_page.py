# Contents of ~/my_app/main_page.py
import streamlit as st
import pandas as pd
from pymongo 
import MongoClient

st.markdown("# Stonkmeizter 🎈")
st.sidebar.markdown("# Stonkomeizter 🎈")

# streamlit_app.py


# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

client = init_connection()


db = client.stonks
collection = db.overall
data = pd.DataFrame(list(collection.find()))
data
