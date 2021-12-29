import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price APP 
Google's stock closing price and volume
""")

ticker_sym = "GOOGL"
ticker_data = yf.Ticker(ticker_sym)
ticker_df = ticker_data.history(period="1d", start="2010-5-31", end="2021-5-31")

st.write("""
## Closing Price
""")
st.line_chart(ticker_df.Close)
st.write("""
## Volume Price
""")
st.line_chart(ticker_df.Volume)
