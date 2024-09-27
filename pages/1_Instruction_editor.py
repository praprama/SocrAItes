import streamlit as st
from openai import OpenAI
from utils.environment import initialize
from utils.auth import menu

st.set_page_config(
    page_title="SocrAItes instruction editor",
    page_icon="icon.jpg",
)

menu()
initialize()
client = OpenAI()
assistant = client.beta.assistants.retrieve("asst_V0S3cfZAOfSqV7ZrC6SB06og")

st.image("icon.jpg", width=100)
st.markdown("# SocrAItes instruction editor")

instructions = st.text_area(label='Assistant Instruction', value=assistant.instructions, height=600)
if st.button('Submit'):
    updated_assistant = client.beta.assistants.update(
        "asst_V0S3cfZAOfSqV7ZrC6SB06og",
        instructions=instructions
    )
    st.rerun()