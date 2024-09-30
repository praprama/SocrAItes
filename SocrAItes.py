import streamlit as st
from openai import OpenAI
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from utils.environment import initialize
from utils.auth import menu
import os, pymongo

st.set_page_config(
    page_title="SocrAItes",
    page_icon="icon.jpg",
)

menu()
initialize()
client = OpenAI()
socraites_agent = OpenAIAssistantRunnable(assistant_id=os.getenv('SOCRAITES_ASST'), as_agent=True)
fainman_agent = OpenAIAssistantRunnable(assistant_id=os.getenv('FAINMAN_ASST'), as_agent=True)

def execute_agent(agent, input):
    response = agent.invoke(input)
    return response.dict()['return_values']['output']

st.image("icon.jpg", width=100)
st.markdown("# Hi. I am SocrAItes. How can I help you?")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread.id

if 'mongo_collection' not in st.session_state:
    MONGO_URL=os.getenv('MONGO_URL')
    myclient = pymongo.MongoClient(MONGO_URL)
    mydb = myclient["socraites"]
    st.session_state.mongo_collection = mydb["conversations"]
    st.session_state.mongo_collection.insert_one({"thread_id": st.session_state.thread_id, "messages": ""})

def update_mongo(role, message):
    doc = st.session_state.mongo_collection.find_one({"thread_id": st.session_state.thread_id})
    messages = doc['messages']
    messages += f'{role.upper()}: {message}\n'
    st.session_state.mongo_collection.find_one_and_update(
        {'thread_id': st.session_state.thread_id},
        {
            '$set': {"messages": messages}
        }
    )

@st.dialog("FAInman Notes of the conversation", width="large")
def fainman_notes():
    with st.spinner("Generating your notes..."):
        doc = st.session_state.mongo_collection.find_one({"thread_id": st.session_state.thread_id})
        messages = doc['messages']
        fainman_response = execute_agent(fainman_agent, {"content": messages})
        st.markdown(fainman_response)

for message in st.session_state.messages:
    if message["role"] == 'user':
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"], avatar='icon.jpg'):
            st.markdown(message["content"])

if prompt := st.chat_input("What is bothering you?"):
    # Add user message to chat history and mongo
    st.session_state.messages.append({"role": "user", "content": prompt})
    update_mongo('user', prompt)
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar='icon.jpg'):
        asst_response = execute_agent(socraites_agent, {"content": prompt, "thread_id": st.session_state.thread_id})
        response = st.markdown(asst_response)
    # Add assistant response to chat history and mongo
    st.session_state.messages.append({"role": "assistant", "content": asst_response})
    update_mongo('teacher', asst_response)

if st.button('Notes'):
    fainman_notes()
