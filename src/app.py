import streamlit as st
from agent import Agent
from dotenv import load_dotenv
import os

st.set_page_config(page_title="The Daily Roast Coffee House", page_icon=":coffee:")

load_dotenv()

open_ai_key = os.getenv("OPENAI_API_KEY")

agent = Agent(open_ai_key)

# Custom global style block for coffee house theme
st.markdown("""
    <style>
        body {
            background-color: #f5f1eb;
            font-family: 'Arial', sans-serif;
        }
        .stTextInput > div > input,
        .stTextArea textarea {
            font-size: 16px;
            background-color: #fffaf5;
            border: 1px solid #d3cfc9;
            color: #3e2c23;
        }
        .stButton>button {
            background-color: #6f4e37;
            color: white;
            border-radius: 4px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #8b5e3c;
        }
        .stChatMessage {
            color: #3e2c23;
        }
        .stMarkdown {
            color: #3e2c23;
        }
        .stSidebar {
            background-color: #e8e1d9;
        }
        .main {             
            background-color: #f7f3ed;
        }
        .stTextArea textarea {
            font-size: 16px;
        }
        .stTextArea label {
            color: #3e2c23;
            font-weight: bold;
        }
        .stAlert {
            color: #3e2c23;
            font-weight: normal;
        }
        p, ul, li, span, blockquote {
            color: #3e2c23 !important;
        }
        button p {
            color: #fff !important;
        }
        textarea {
            height: 80px !important;
            font-size: 18px !important;
            background-color: #fffefb !important;
            border: 2px solid #6f4e37 !important;
            color: #3e2c23 !important;
            padding: 10px !important;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown("""
    <h1 style='text-align: center; font-size: 36px; color: #6f4e37;'>Welcome to The Daily Roast Coffee House ☕</h1>
    <p style='text-align: center; color: #6f4e37;'>I'm your virtual coffee seller. Ask me anything about our menu!</p>
""", unsafe_allow_html=True)

# Chat-based interaction using st.chat_message and session state for history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("### Chat with our AI virtual barista")

# If there are no messages yet, show a centered info box encouraging interaction
if not st.session_state.messages:
    with st.container():
        st.markdown(
            """
            <div style='text-align: center; padding: 50px 0; color: #6f4e37;'>
                <h2 style='font-size: 28px;'>No messages yet ☕</h2>
                <p style='font-size: 18px;'>Ask me anything about our coffee options, origins, or recommendations!</p>
                <p style='font-size: 16px;'>Try something like <em>"What is the most popular blend?"</em></p>
            </div>
            """,
            unsafe_allow_html=True
        )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("What can I get started for you today?")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Brewing your coffee..."):
        response = agent.get_coffee_answer(user_input)
        assistant_response = response["coffee"]
    st.chat_message("assistant").markdown(assistant_response)
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

