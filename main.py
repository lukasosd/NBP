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
st.subheader("This app downloads the day before invoice date exchange rate from "
             "the NBP website and calculates the given amount to PLN.")
date = st.text_input(label="Please insert invoice date below(from 01.01.2002):",
                     placeholder="DD.MM.YYYY", key='invoice_date')
currency = st.selectbox('Please insert currency below:', (currencies))
amount = st.text_input(label="Please insert amount below:",
                       placeholder="E.g. 10000.00", key='amount')

if (st.button('Submit')):
    try:
        calculate(currency, date, amount)
    except:
        st.error('Incorrect data')


