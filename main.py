from selenium import webdriver
import time
import streamlit as st
from bs4 import BeautifulSoup as soup

# Replace with your chromedriver.exe path
driver = webdriver.Chrome(executable_path='C:/Users/nitro 5/Downloads/chromedriver.exe')

# Website from which nifty50 price will be scraped
url = 'https://finance.yahoo.com/quote/%5ENSEI/'
driver.get(url)

st.set_page_config(
    page_title = 'Real-Time Dashboard',
    page_icon = '✅',
    layout = 'wide'
)
st.title("Nifty50 Live Dashboard")
st.write('---')

placeholder = st.empty()

while 1:
    html = driver.page_source
    page_soup = soup(html,features="lxml")
    nifty50 = page_soup.find("div", {"class": "D(ib) Mend(20px)"}).text
    my_list = nifty50.split()
    print(my_list)
    nifty50_price = my_list[0].split('+')[0]
    nifty50_time = my_list[3][0:5]

    with placeholder.container():
        price1, price2 = st.columns(2)
        price1.metric(label='Price', value=nifty50_price)
        price2.metric(label='Time', value=nifty50_time)

    time.sleep(1)
