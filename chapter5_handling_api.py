import streamlit as st
import requests

# rupees to other currency converter

options  = [
"AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN",
"BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL",
"BSD","BTN","BWP","BYN","BZD","CAD","CDF","CHF","CLF","CLP",
"CNH","CNY","COP","CRC","CUP","CVE","CZK","DJF","DKK","DOP",
"DZD","EGP","ERN","ETB","EUR","FJD","FKP","FOK","GBP","GEL",
"GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HRK",
"HTG","HUF","IDR","ILS","IMP","IQD","IRR","ISK","JEP","JMD",
"JOD","JPY","KES","KGS","KHR","KID","KMF","KRW","KWD","KYD",
"KZT","LAK","LBP","LKR","LRD","LSL","LYD","MAD","MDL","MGA",
"MKD","MMK","MNT","MOP","MRU","MUR","MVR","MWK","MXN","MYR",
"MZN","NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB","PEN",
"PGK","PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF",
"SAR","SBD","SCR","SDG","SEK","SGD","SHP","SLE","SLL","SOS",
"SRD","SSP","STN","SYP","SZL","THB","TJS","TMT","TND","TOP",
"TRY","TTD","TVD","TWD","TZS","UAH","UGX","USD","UYU","UZS",
"VES","VND","VUV","WST","XAF","XCD","XCG","XDR","XOF","XPF",
"YER","ZAR","ZMW","ZWG","ZWL"
]

st.title("my streamlit currency converter")
choice = st.selectbox("Select in the output currency: ", options)

amount = st.number_input("Enter your amount for conversion: ", min_value=1)

response = requests.get("https://open.er-api.com/v6/latest/INR")

if response.status_code == 200:
    data = response.json()  # converting json data to dict
    rate = data['rates'][choice]
    result = rate * amount
    st.success(f"{amount} INR = {result:.3f} {choice}")
else:
    st.error("Falied to fetch the data")