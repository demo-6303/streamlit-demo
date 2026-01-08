import streamlit as st

st.title("select a layout")

col1, col2, col3 = st.columns(3)  # every column is treated as independent age

with col1:
    vote1 = st.button("option 1")
    # we can add images also
    st.image("https://images.pexels.com/photos/35403154/pexels-photo-35403154.jpeg", width = 100)

with col2:
    vote2 = st.button("Option 2")
     # we can add images also
    st.image("https://images.pexels.com/photos/35403154/pexels-photo-35403154.jpeg", width = 400)

with col3:
    vote3 = st.button("Option 3")
     # we can add images also
    st.image("https://images.pexels.com/photos/35403154/pexels-photo-35403154.jpeg", width = 400)

if vote1:
    st.write("you have selected layout 1")
elif vote2:
    st.write("You have selected layout 2")
elif vote3:
    st.write("You have selected layout 3")


# adding a sidebar

name = st.sidebar.text_input("Enter your name:")  # we just need to use st.sidebar to work in side bar

st.sidebar.write(f"You have entered {name}")
st.write(f"You have entered {name}")  # we can use sidebar content in main layout also

st.sidebar.expander(""" 
    This is my expender content in sidebar
""")

st.markdown("### This is markdown")
st.markdown("> option one in markdown")

