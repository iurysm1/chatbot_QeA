from dataclasses import dataclass
from typing import Literal
import streamlit as st
import streamlit.components.v1 as components
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from memory import enviar_mensagem
import time
from render_msg import render_chat


file=None

@dataclass
class Message:
    origin: Literal["human", "ai"]
    message: str

def load_css():
    with open("static/styles.css", "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)

def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []


def on_click_callback():
    if uploaded_file is not None:
        human_prompt = st.session_state.human_prompt
        llm_response = enviar_mensagem(human_prompt, file)
        st.session_state.history.append(
            Message("human", human_prompt)
        )
        st.session_state.history.append(
            Message("ai", llm_response)
        )
 


load_css()
initialize_session_state()

st.title("Seu assistente pessoal! 🤖")

chat_placeholder = st.container()
prompt_placeholder = st.form("chat-form")
credit_card_placeholder = st.empty()

with chat_placeholder:
    chat_html = render_chat(st.session_state.history)
    st.markdown(chat_html, unsafe_allow_html=True)


uploaded_file = st.file_uploader("Escolha um arquivo")
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_filename = temp_file.name
    loader = PyPDFLoader(temp_filename)
    file = loader

with prompt_placeholder:
    st.markdown("**Chat**")
    cols = st.columns((6, 1))
    cols[0].text_input(
        "Chat",
        value="Hello bot",
        label_visibility="collapsed",
        key="human_prompt",
    )
    cols[1].form_submit_button(
        "Submit", 
        type="primary", 
        on_click= on_click_callback, 
    )




components.html("""
<script>
const streamlitDoc = window.parent.document;

const buttons = Array.from(
    streamlitDoc.querySelectorAll('.stButton > button')
);
const submitButton = buttons.find(
    el => el.innerText === 'Submit'
);

streamlitDoc.addEventListener('keydown', function(e) {
    switch (e.key) {
        case 'Enter':
            submitButton.click();
            scrollToBottom()
            break;
    }
});


</script>

""", 
    height=0,
    width=0,
)


