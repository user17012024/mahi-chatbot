import streamlit as st

st.title("💬 Mahi ka Chatbot")

# user se input lena
user_input = st.text_input("Aapka message likhiye:")

# response dikhana
if user_input:
    st.write("AI Friend 🤖: Haan ji! Aapne bola → " + user_input)
