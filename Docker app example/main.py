import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client (pointing to local Docker Model Hub)
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")  # may be a dummy key if not required by Docker Model Hub
)

# Streamlit UI
st.set_page_config(page_title="UCU DevOps LLM App", layout="centered")
st.title("UCU DevOps Course — Simple LLM App")

if 'history' not in st.session_state:
    st.session_state.history = []

# Input prompt
prompt = st.text_area("Enter your prompt", "Explain how transformers work.")

if st.button("Send"):
    with st.spinner("Getting response..."):
        messages = [{"role": "user", "content": prompt}]
        try:
            response = client.chat.completions.create(
                model=os.getenv("MODEL"),
                messages=messages
            )

            # Extract response text
            if response.choices and len(response.choices) > 0:
                reply = response.choices[0].message.content
            else:
                reply = "[No response from model]"

            st.session_state.history.append((prompt, reply))
            st.success("Response received!")

        except Exception as e:
            st.error(f"Error: {e}")

# Show conversation history
st.subheader("Conversation History")
for i, (q, a) in enumerate(st.session_state.history, 1):
    st.markdown(f"**You ({i}):** {q}")
    st.markdown(f"**Assistant ({i}):** {a}")
  
