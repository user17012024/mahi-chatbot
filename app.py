
import streamlit as st
from transformers import pipeline

st.title("🤖 Mahi ka AI Chatbot (Practice Version)")

# Hugging Face model load karna (GPT-2 use kar rahe hain)
chatbot = pipeline("text-generation", model="gpt2")

# user input
user_input = st.text_input("Aapka message likhiye:")

if user_input:
    response = chatbot(user_input, max_length=50, num_return_sequences=1, do_sample=True)[0]["generated_text"]
    st.write("AI Friend 💬: " + response)
