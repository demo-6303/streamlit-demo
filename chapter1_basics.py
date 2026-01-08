import streamlit as st

# basics

st.title("This is my app")
st.subheader("This is my sub header")

st.text("This is my text")
st.write("This is write")

mychoice = st.selectbox("which game do you like? ", ["Hockey", "chess", "Football", "Cricket"])

st.write(f"You have selected {mychoice}. great choice!!")

st.success(f"Thanks for using {mychoice}")

st.success("Thanks for using our service")