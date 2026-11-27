
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: white;
    }
    h1 {
        text-align: center;
        color: #8ab4f8;
    }
    .subtitle {
        text-align: center;
        color: #b0b8c4;
        margin-bottom: 25px;
    }
</style>
""", unsafe_allow_html=True)

# App heading
st.title("🤖 AI Chatbot")
st.markdown(
    '<p class="subtitle">Powered by Streamlit & Groq AI</p>',
    unsafe_allow_html=True
)

# API key input in the sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = os.getenv("GROQ_API_KEY")

    st.caption("Your API key is not saved by this app.")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Welcome message
if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.write(
            "Hello! 👋 I'm your AI assistant. "
            "Ask me anything to get started!"
        )

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Type your message here...")

if prompt:
    # Show the user's message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Validate API key
    if not api_key:
        st.warning(
            "Please enter your Groq API key in the sidebar first."
        )
        st.stop()

    try:
        client = Groq(api_key=api_key)

        # Generate AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a helpful, friendly AI assistant. "
                                "Give clear, accurate and useful answers."
                            )
                        },
                        *st.session_state.messages
                    ],
                    temperature=0.7,
                    max_tokens=1024
                )

                answer = response.choices[0].message.content
                st.markdown(answer)

        # Save the assistant response
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

    except Exception as e:
        st.error(
            "Something went wrong. Check your API key, "
            "internet connection, Groq model availability, "
            "or API usage limits."
        )
        st.caption(f"Error details: {e}")
