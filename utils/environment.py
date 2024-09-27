import streamlit as st
import os

def initialize():
    os.environ["OPENAI_API_KEY"] = st.secrets.OPENAI_API_KEY
    os.environ["LANGCHAIN_API_KEY"] = st.secrets.LANGCHAIN_API_KEY
    os.environ["LANGCHAIN_TRACING_V2"] = 'true'
    os.environ["LANGCHAIN_PROJECT"] = 'socraites'