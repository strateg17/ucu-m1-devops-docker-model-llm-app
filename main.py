import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

##############################
# SETTINGS
##############################

load_dotenv(override=True)


# Load From .env File
LOCAL_MODEL_NAME = os.getenv("LOCAL_MODEL_NAME", "missing-model-name")
LOCAL_BASE_URL = os.getenv("LOCAL_BASE_URL", "missing-base-url")

if "missing" in LOCAL_MODEL_NAME or "missing" in LOCAL_BASE_URL:
    st.error(f"Missing environment variables: LOCAL_MODEL_NAME={LOCAL_MODEL_NAME}, LOCAL_BASE_URL={LOCAL_BASE_URL}")

# Initialize Local Model
local_llm = ChatOpenAI(
    model=LOCAL_MODEL_NAME,
    api_key="nope",  # must be set, even dummy
    base_url=LOCAL_BASE_URL
)

##############################
# GUI
##############################

st.title("UCU Test app chat...")

# Initialize Chat Message Memory
st.session_state.setdefault("messages", [])

# Display Chat Message History from Memory
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Collect User Prompt
prompt = st.chat_input("Type your message...")

# If New User Prompt was Submitted
if prompt:
    # Add the New User Prompt to Memory
    st.session_state["messages"].append(
        {"role": "user", "content": prompt}
    )
    with st.chat_message("user"):
        st.write(prompt)
    
    # Combine Chat History as Context to the New Prompt
    context = "\n".join(
        f"{msg['role']}: {msg['content']}"
        for msg in st.session_state["messages"]
    )
    
    # Generate Model Response from User Prompt + Context
    response = local_llm.invoke(context)
    
    # Add the New Model Response to Memory
    st.session_state["messages"].append(
        {"role": "assistant", "content": response.content}
    )
    with st.chat_message("assistant"):
        st.write(response.content)
