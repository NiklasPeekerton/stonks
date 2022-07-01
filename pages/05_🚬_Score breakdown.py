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
import plotly.express as px

st.set_page_config(layout="wide")


st.markdown("# Score breakdown 🚬")
st.sidebar.markdown("# Score breakdown 🚬")


def get_client():
    return MongoClient(**st.secrets["mongo"])

client = get_client()
db = client.stonks

@st.experimental_memo
def metric():
    collection = db.enterprisevalue
    industry = collection.find()
    df = pd.DataFrame(industry)
    df = df.drop(columns=['_id'])
    #df = df.astype({" Industry": str})
    #logdf = df.sort_values(by=['Market Capitalization size'], ascending=False)
    #logdf = logdf[:-6]
    #df = df.sort_values(by=['Overall points'], ascending=False)
    #st.dataframe(df)

    df20 = df.head(20)
    #df20 = df20.sort_values(by=['Overall points'], ascending=True)
    return df, logdf, df20

allindustries = metric()[0]

st.write(allindustries)

