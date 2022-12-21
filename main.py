import streamlit as st
import functions

currencies = ('EUR', 'USD', 'CHF')
def calculate(currency, date, amount):
    new_date = functions.day_before(date)
    exchange_rate = functions.cur_import(currency,new_date)
    message = functions.result(exchange_rate, amount)
    global text
    text = st.text_area('Result', value=message)

st.set_page_config(layout="wide")

st.markdown(""" <style> .font {
font-size:60px ; font-family: 'Cooper Black'; color: #3230b8;} 
</style> """, unsafe_allow_html=True)
st.markdown('<p class="font">CURRENCY CONVERTER</p>', unsafe_allow_html=True)
st.subheader("This app downloads the exchange rate from  the NBP website and "
             "calculates the given amount to PLN.")
st.write("Please insert invoice date below(from 2002-01-01):")
date = st.text_input(label="", placeholder="YYYY-MM-DD", key='invoice_date')
st.write("Please insert currency below:")
currency = st.st.selectbox("Please insert currency below:", (currencies))
st.write("Please insert amount below:")
amount = st.text_input(label="", placeholder="E.g. 10000.00", key='amount')

if (st.button('Submit')):
    calculate(currency, date, amount)


