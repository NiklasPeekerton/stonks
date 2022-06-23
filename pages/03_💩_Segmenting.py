# Contents of ~/my_app/main_page.py
import streamlit as st
import pandas as pd
import pymongo
#import pymongo[srv]
from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np
import altair as alt

st.markdown("# Segmentazione 💩")
st.sidebar.markdown("# Segment 💩")


def get_client():
    return MongoClient(**st.secrets["mongo"])

client = get_client()


db = client.stonks
collection = db.overall2
data = collection.find()

st.dataframe(data)
