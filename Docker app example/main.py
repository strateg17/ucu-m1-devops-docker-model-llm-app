import os
import streamlit as st

from openai import OpenAI
from dotenv import load_dotenv

#load ENV variables
load_doteanv()

# Initialize OpenAI client
client = OpenAI(
  base_url=os.getenv("BASE_URL"),
  api_key=os.getenv("API_KEY")
)

# Streamlit UI
st.title("UCU DevOps course simple LLM app")
prompt = st.text_area("Enter your prompt", "Explain how transformers work.")

if st.button("Send"):
  with st.spinner("Getting response..."):
    messages = [
      {"role": "user", "content": prompt}
    ]
    try:
      reponse = client.chat.completions.create(
        model = os.getenv("MODEL"),
        messages = messages
      )
      st.success("Response:")
      

