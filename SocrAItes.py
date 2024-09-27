import streamlit as st
from openai import OpenAI
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from utils.environment import initialize

st.set_page_config(
    page_title="SocrAItes",
    page_icon="icon.jpg",
)

initialize()
client = OpenAI()
#assistant = client.beta.assistants.retrieve("asst_V0S3cfZAOfSqV7ZrC6SB06og")
agent = OpenAIAssistantRunnable(assistant_id="asst_V0S3cfZAOfSqV7ZrC6SB06og", as_agent=True)

def execute_agent(input):
    response = agent.invoke(input)
    return response.dict()['return_values']['output']

st.image("icon.jpg", width=100)
st.markdown("# Hi. I am SocrAItes. How can I help you?")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread.id

for message in st.session_state.messages:
    if message["role"] == 'user':
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"], avatar='icon.jpg'):
            st.markdown(message["content"])

if prompt := st.chat_input("What is bothering you?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar='icon.jpg'):
        asst_response = execute_agent({"content": prompt, "thread_id": st.session_state.thread_id})
        response = st.markdown(asst_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": asst_response})
