import streamlit as st
import random

st.title("💬 Mahi ka Personal Chatbot")

# simple replies database
responses = {
    "hi": ["Hello!", "Hiii 😃", "Hey! Kya haal hai?"],
    "kaise ho": ["Main bilkul mast! 😎", "Awesome! Aur tum?", "Theek hu, tum sunao 💖"],
    "bye": ["Bye bye 👋", "Phir milte hain!", "Take care ❤️"],
}

# user input
user_input = st.text_input("Aapka message likhiye:")

# response generate karna
if user_input:
    msg = user_input.lower()
    reply = None
    for key in responses:
        if key in msg:
            reply = random.choice(responses[key])
            break
    if not reply:
        reply = "Hmm... interesting 😅 aur batao!"
    
    st.write("AI Friend 🤖: " + reply)
