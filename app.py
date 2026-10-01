import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
You are a helpful and friendly AI assistant.
Answer clearly and in simple English.
Keep your answers concise unless the user asks for more detail.
"""

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
)

st.title("AI Chatbot")
st.caption("simple chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_message = st.chat_input("Type your message here...")

if user_message:

    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    with st.chat_message("user"):
        st.write(user_message)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = client.responses.create(
                model="gpt-4o-mini",
                instructions=SYSTEM_PROMPT,
                input=st.session_state.messages
            )

            assistant_message = response.output_text

            st.write(assistant_message)

    st.session_state.messages.append({
        "role": "assistant",
        "content": assistant_message
    })