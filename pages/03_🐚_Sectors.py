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

st.markdown("# Sectors 🐚")
st.sidebar.markdown("# Sectors 🐚")


def get_client():
    return MongoClient(**st.secrets["mongo"])

client = get_client()
db = client.stonks

@st.experimental_memo
def sectormean():
    collection = db.sectorsmean
    sector = collection.find()
    df = pd.DataFrame(sector)
    df = df.drop(columns=['_id'])
    df = df.astype({" Sector": str})
    logdf = df.sort_values(by=['Market Capitalization size'], ascending=False)
    logdf = logdf[:-1]
    df = df.sort_values(by=['Overall points'], ascending=False)
    #st.dataframe(df)

    df20 = df.head(20)
    df20 = df20.sort_values(by=['Overall points'], ascending=True)
    return df, logdf, df20

allsectors = sectormean()[0]
logsectors = sectormean()[1]
top20sectors = sectormean()[2]

fig = px.bar(top20sectors, x=["Dividend points normal", "Revenues points normal", "Free Cash Flow points normal", 'Net Income points normal', 
                    'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 
                    'Payout Ratio points normal'], y=" Sector", title="Industries sorted by average overall points broken down my metric",
            labels=dict(value="Average overall points", variable="Metrics"), height=600
            )
st.plotly_chart(fig, use_container_width=True)





valuepoints = px.scatter(logsectors, x="Market Capitalization size", y="Overall points", color=' Sector', 
                         log_y=True, log_x=True, trendline="ols",
                         trendline_options=dict(log_x=True, log_y=True), 
                         trendline_scope="overall", text=' Sector',
                         title="Log scale of market cap by overall points. The size of the bubbles are based on the Free cash flow points",
                         labels=dict(value="Average market Capitalization size", y="Average overall points"),
                         #width=800, 
                         height=900,
                         size='Free Cash Flow points normal',
                         hover_name=" Sector"
                )



valuepoints.update_xaxes(type="log", range=[np.log10(13000), np.log10(11000000000)])
valuepoints.update_yaxes(type="log", range=[np.log10(140), np.log10(400)])
st.plotly_chart(valuepoints, use_container_width=True)

st.dataframe(allsectors)



@st.experimental_memo
def sectormetric(sector):
    collection = db.overall2
    overall = collection.find({' Sector': sector })
    df = pd.DataFrame(overall)
    df = df.astype({" Sector": str})
    df = df[['Overall points', 'Market Capitalization size','Name', 'Ticker', ' Sector', 'Dividend points normal', 'Revenues points normal', 'Free Cash Flow points normal', 'Net Income points normal',
     'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 'Payout Ratio points normal'#, 'Website'
        ]]

    df = df.loc[df[' Sector'] == sector]
    df = df.drop(columns=[' Sector'])


    df20 = df.head(25)
    df20 = df20.sort_values(by=['Overall points'], ascending=True)

    df = df.astype({"Name": str})

    return df, df20



sectorlist = allsectors[' Sector'].tolist()

options = st.selectbox(
     'Pick a sector you want to see stats for',
     sectorlist#,
#     #sectorlist[69]
)

st.subheader(options)

full = sectormetric(options)[0]
top20 = sectormetric(options)[1]

fig = px.bar(top20, x=["Dividend points normal", "Revenues points normal", "Free Cash Flow points normal", 'Net Income points normal', 
                        'Net Income Margin points normal', 'Current Ratio points normal', 'Weighted Average Shares (Diluted) points normal', 
                        'Payout Ratio points normal'], y="Ticker", title=options+" tickers sorted by average overall points broken down my metric", text='Overall points',
                labels=dict(value="Average overall points", variable="Metrics"),
                 height=600
                )


test = full.describe()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Number of stocks", test.loc['count'][0])
col2.metric("Average score", test.loc['mean'][0])
col3.metric("Min score", test.loc['min'][0])
col4.metric("Max score", test.loc['max'][0])

col5, col6, col7 = st.columns(3)
col5.metric("25% score", test.loc['25%'][0])
col6.metric("50% score", test.loc['50%'][0])
col7.metric("75% score", test.loc['75%'][0])

def make_clickable(val):
    return f'<a target="_blank" href="{val}">{val}</a>'
    
st.plotly_chart(fig, use_container_width=True)
styledf = full.style.format({"Market Capitalization size": '${0:,.2f}', "Overall points": "🏆{:20,.0f}"
                         , "Dividend points normal": "🏆{:20,.0f}", "Revenues points normal": "🏆{:20,.0f}"
                         , "Free Cash Flow points normal": "🏆{:20,.0f}", "Net Income points normal": "🏆{:20,.0f}"
                         , "Net Income Margin points normal": "🏆{:20,.0f}", "Current Ratio points normal": "🏆{:20,.0f}"
                         , "Weighted Average Shares (Diluted) points normal": "🏆{:20,.0f}", "Payout Ratio points normal": "🏆{:20,.0f}"#,
                          #'Website': make_clickable
                         
                         }, hyperlinks='html')\
                 .hide_index()\
                 .bar(subset=["Overall points"], color='1B2432')\
                 .bar(subset=["Market Capitalization size"], color='lightgreen')\
                 .bar(subset=["Revenues points normal"], color='#EF553B')\
                 .bar(subset=["Dividend points normal"], color='#646FFB')\
                 .bar(subset=["Free Cash Flow points normal"], color='#00CC96')\
                 .bar(subset=["Net Income points normal"], color='#AB63FA')\
                 .bar(subset=["Net Income Margin points normal"], color='#FFA15A')\
                 .bar(subset=["Current Ratio points normal"], color='#19D3F3')\
                 .bar(subset=["Weighted Average Shares (Diluted) points normal"], color='#FF6692')\
                 .bar(subset=["Payout Ratio points normal"], color='#B6E980')

                 #.background_gradient(cmap='Blues')
                     
#test1 =  test.style.format({'Name': make_clickable_both}).bar(subset=['Overall points'], align='mid', color=['#d65f5f', '#5fba7d'])
#st.table(test)
st._legacy_dataframe(styledf, height=800)
#st.markdown(
#    test_styled.to_html(table_uuid="table_1"), unsafe_allow_html=True
#)

#test['Market Capitalization size'] = test['Market Capitalization size'].apply(lambda x: f'${x/1000000:.1f}M' if x/1000000>=1 else f'${int(x/1000)}K' if x/10000>=1 else f'${x}')
#st._legacy_dataframe(test)
