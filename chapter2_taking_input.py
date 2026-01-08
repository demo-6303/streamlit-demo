import streamlit as st

# widgets

# button

if st.button("click here"):         # we get response as bool
    st.write("thanks for clicking")

# checkbox

myvar = st.checkbox("Select this checkcbox: ")

if myvar:
    st.write("you have selected the box")


# radio button 

mychoice = st.radio("Select your choice: ", ["option 1", "option 2", "option 3"])

st.write(f"Ypu have selected {mychoice}")

# select box

mychoice = st.selectbox("which game do you like? ", ["Hockey", "chess", "Football", "Cricket"])
st.write(f"You have selected {mychoice}. great choice!!")

# slider

level = st.slider("Select your level : ", 0,5,3)  # start, end, defalut
st.write(f"You have set level to {level}")  

# geting numeric input

num = st.number_input("Enter your number choice: ", min_value = 0, max_value = 100, step = 2)
st.write(f"You have selected {num}")

# getting text input

myname = st.text_input("Enter your name: ")
st.write(f"Welcome {myname}")

# getting dob

mydob = st.date_input("Select your date of birth: ")
st.write(f"Your dob is {mydob}")
