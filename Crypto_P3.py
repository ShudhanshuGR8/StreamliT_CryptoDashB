#importing neccessary libraries
from turtle import width
import yfinance as yf
import streamlit as st
from PIL  import Image
from urllib.request import urlopen
from datetime import date
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
st.set_page_config(page_title='Crypto-Analysis', layout = "centered")

def main():
    page = st.sidebar.selectbox(
        "Crypto-Market",
        [
            "Cryptocurrency Prices",
            "Analysis and Visualization"
        ]
    )

    if page == "Cryptocurrency Prices":
        homepage()
    elif page == "Analysis and Visualization":
        visualz()
today = date.today()
week_ago = today - dt.timedelta(days=7)

def homepage():

    #Titles and Headings?
    st.title("Cryptocurrency Analysis - OPEN")
    st.header("Dashboard")
    st.markdown(""" <style>
    </style> """, unsafe_allow_html=True)


    #Defining ticker variables
    Bitcoin = 'BTC-INR'
    Ethereum = 'ETH-INR'
    Ripple = 'XRP-INR'
    BitcoinCash = 'BCH-INR'
    Cardano = 'ADA-INR'

    # Data accessing from Yahoo Finance
    BTC_Data = yf.Ticker(Bitcoin)
    ETH_Data = yf.Ticker(Ethereum)
    XRP_Data = yf.Ticker(Ripple)
    BCH_Data = yf.Ticker(BitcoinCash)
    ADA_Data = yf.Ticker(Cardano)

    #Data Fetching from Yahoo Finance
    BTC_His = BTC_Data.history(period = 'max')
    ETH_His = ETH_Data.history(period = 'max')
    XRP_His = XRP_Data.history(period = 'max')
    BCH_His = BCH_Data.history(period = 'max')
    ADA_His = ADA_Data.history(period = 'max')

    #Fetching Crypto Data from Data Frame
    BTC = yf.download(Bitcoin, start=week_ago, end=today)
    ETH = yf.download(Ethereum, start=week_ago, end=today)
    XRP = yf.download(Ripple, start=week_ago, end=today)
    BCH = yf.download(BitcoinCash, start=week_ago, end=today)
    ADA = yf.download(Cardano, start = week_ago, end=today)
    BTC_Close = BTC['Close']
    ETH_Close = ETH['Close']
    XRP_Close = XRP['Close']
    BCH_Close = BCH['Close']
    ADA_Close = ADA['Close']

    #Bitcoin
    st.subheader("Bitcoin (INR)")
    imageBTC = Image.open(urlopen('https://pngimg.com/uploads/bitcoin/bitcoin_PNG48.png'))

    #Display Image
    st.image(imageBTC, width = 240)

    #Display Dataframe
    st.table(BTC)

    #Display a Chart
    st.area_chart(BTC_His.Close)
    st.markdown("***")



    #Ethereum
    st.subheader("Ethereum (INR)")
    imageETH = Image.open(urlopen('https://www.pngall.com/wp-content/uploads/10/Ethereum-Logo-PNG.png'))

    #Display Image
    st.image(imageETH, width = 240)

    #Display Dataframe
    st.table(ETH)

    #Display a Chart
    st.area_chart(ETH_His.Close)
    st.markdown("***")



    #Ripple
    st.subheader("Ripple (INR)")
    imageXRP = Image.open(urlopen('https://ripple.com/wp-content/uploads/2020/07/ripple-triskelion-512.png'))

    #Display Image
    st.image(imageXRP, width = 240)

    #Display Dataframe
    st.table(XRP)

    #Display a Chart
    st.area_chart(XRP_His.Close)
    st.markdown("***")



    #BitcoinCash
    st.subheader("BitcoinCash (INR)")
    imageBCH = Image.open(urlopen('https://upload.wikimedia.org/wikipedia/commons/5/58/Bitcoin_Cash.png'))

    #Display Image
    st.image(imageBCH, width = 240)

    #Display Dataframe
    st.table(BCH)

    #Display a Chart
    st.area_chart(BCH_His.Close)

    #Cardano
    st.subheader("Cardano (INR)")
    imageADA = Image.open(urlopen('https://cdn4.iconfinder.com/data/icons/crypto-currency-and-coin-2/256/cardano_ada-512.png'))

    #Display Image
    st.image(imageADA, width = 240)

    #Display Dataframe
    st.table(ADA)

    #Display a Chart
    st.area_chart(ADA_His.Close)
    st.markdown("***")



def visualz():
    Bitcoin = 'BTC-INR'
    Ethereum = 'ETH-INR'
    Ripple = 'XRP-INR'
    BitcoinCash = 'BCH-INR'
    Cardano = 'ADA-INR'

    BTC_Data = yf.Ticker(Bitcoin)
    ETH_Data = yf.Ticker(Ethereum)
    XRP_Data = yf.Ticker(Ripple)
    BCH_Data = yf.Ticker(BitcoinCash)
    ADA_Data = yf.Ticker(Cardano)

    #Data Fetching from Yahoo Finance
    BTC_His = BTC_Data.history(period = 'max')
    ETH_His = ETH_Data.history(period = 'max')
    XRP_His = XRP_Data.history(period = 'max')
    BCH_His = BCH_Data.history(period = 'max')
    ADA_His = ADA_Data.history(period = 'max')

    #Fetching Crypto Data from Data Frame
    BTC = yf.download(Bitcoin, start=week_ago, end=today)
    ETH = yf.download(Ethereum, start=week_ago, end=today)
    XRP = yf.download(Ripple, start=week_ago, end=today)
    BCH = yf.download(BitcoinCash, start=week_ago, end=today)
    ADA = yf.download(Cardano, start = week_ago, end=today)
    BTC_Close = BTC['Close']
    ETH_Close = ETH['Close']
    XRP_Close = XRP['Close']
    BCH_Close = BCH['Close']
    ADA_Close = ADA['Close']


    st.subheader("Below are the Visualizations performed by OPEN Team:   ")
    st.header(" ")
    image1 = Image.open("images/Analysis_1.png")
    st.image(image1)
    image2 = Image.open("images/Analysis_3.png")
    st.image(image2)
    image3 = Image.open("images/Analysis_4.png")
    st.image(image3)
    image4 = Image.open("images/Analysis_5.png")
    st.image(image4)
    image5 = Image.open("images/Analysis_6.png")
    st.image(image5)
    image6 = Image.open("images/Analysis_7.png")
    st.image(image6)
    image7 = Image.open("images/Analysis_8.png")
    st.image(image7)
    image8 = Image.open("images/Analysis_9.png")
    st.image(image8)
    image9 = Image.open("images/Analysis_10.png")
    st.image(image9)
    image10 = Image.open("images/Analysis_11.png")
    st.image(image10)
    image11 = Image.open("images/Analysis_12.png")
    st.image(image11)
    image12 = Image.open("images/Analysis_13.png")
    st.image(image12)
    image13 = Image.open("images/Analysis_14.png")
    st.image(image13)
    image14 = Image.open("images/Analysis_15.png")
    st.image(image14)
    image15 = Image.open("images/Analysis_16.png")
    st.image(image15)
    image16 = Image.open("images/Analysis_17.png")
    st.image(image16)

if __name__ == "__main__":
    main()