import streamlit as st
from openai import OpenAI
from utils.environment import initialize
from utils.auth import menu, menu_with_redirect
import os

st.set_page_config(
    page_title="SocrAItes instruction editor",
    page_icon="icon.jpg",
)

# Uncomment below line and comment menu() once auth is enabled in the main page
# menu_with_redirect()
menu()

# Verify the user's role
if st.session_state.role not in ["admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

initialize()
client = OpenAI()
socraites_assistant = client.beta.assistants.retrieve(os.getenv('SOCRAITES_ASST'))

st.image("icon.jpg", width=100)
st.markdown("# SocrAItes instruction editor")

socraites_instructions = st.text_area(label='SocrAItes Assistant Instruction', value=socraites_assistant.instructions, height=600)
if st.button('Submit', key='socraites'):
    updated_assistant = client.beta.assistants.update(
        os.getenv('SOCRAITES_ASST'),
        instructions=socraites_instructions
    )
    st.rerun()

socraites_suggestive = client.beta.assistants.retrieve(os.getenv('SOCRAITES_SUGGESTIVE'))
socraites_sugestive_instructions = st.text_area(label='SocrAItes Suggestive Instruction', value=socraites_suggestive.instructions, height=600)
if st.button('Submit', key='socraites_suggestive'):
    updated_assistant = client.beta.assistants.update(
        os.getenv('SOCRAITES_SUGGESTIVE'),
        instructions=socraites_sugestive_instructions
    )
    st.rerun()

fainman_assistant = client.beta.assistants.retrieve(os.getenv('FAINMAN_ASST'))
fainman_instructions = st.text_area(label='FAInman Assistant Instruction', value=fainman_assistant.instructions, height=600)
if st.button('Submit', key='fainman'):
    updated_assistant = client.beta.assistants.update(
        os.getenv('FAINMAN_ASST'),
        instructions=fainman_instructions
    )
    st.rerun()