import streamlit as st
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from chains.cfu_chain import cfu_chain
from chains.note_evaluator import eval_chain
import pandas as pd

fainman_agent = OpenAIAssistantRunnable(assistant_id='asst_mFjrLvmyIo1GArF2VONdXu46', as_agent=True)

def execute_agent_notools(agent, input):
    response = agent.invoke(input)
    return response.dict()['return_values']['output']

@st.dialog(" ", width="large")
def text_dialog(text):
    st.markdown(text)

def cfu():
    st.image("icon.jpg", width=100)
    st.markdown("# Let's make sure you have your notes by answering a set of questions")

    #doc = st.session_state.mongo_collection.find_one({"thread_id": 'thread_fcKnOmbsNL4xI2cpkDPiNSkU'})
    doc = st.session_state.mongo_collection.find_one({"thread_id": st.session_state.thread_id})
    messages = doc['messages']

    if 'submitted' not in st.session_state:
        st.session_state.submitted = []

    if 'feynman_notes' not in st.session_state:
        with st.spinner("Parsing your conversation.."):
            st.session_state.feynman_notes = execute_agent_notools(fainman_agent, {"content": messages})
    
    if 'cfu_questions' not in st.session_state:
        with st.spinner("Generating your questions..."):
            res = cfu_chain.invoke(st.session_state.feynman_notes)
            st.session_state.cfu_questions = res['cfu_questions']
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("View transcript"):
            text_dialog(messages)
    with col2:
        if st.button("View Feynman notes"):
            text_dialog(st.session_state.feynman_notes)

    #questions_df = pd.DataFrame().from_dict(st.session_state.cfu_questions)
    #tab_labels = questions_df['section'].tolist()

    #for tab in st.tabs(tab_labels):
    #    with tab:
    
    for q in range(0, len(st.session_state.cfu_questions)):
        elem = st.session_state.cfu_questions[q]
        answer = st.text_area(label=f"{str(q)}. {elem['question']}", height=150)
        if st.button('Save', key=q):
            res = eval_chain.invoke({"feynman_notes": st.session_state.feynman_notes, "question": elem['question'], "answer": answer})
            st.write(res)
            if q not in st.session_state.submitted:
                st.session_state.submitted.append(q)

    # Uncomment following if we want to show notes after all questions are answered
    #if len(st.session_state.submitted) == len(st.session_state.cfu_questions):
    #    if st.button("View Feynman notes"):
    #        text_dialog(st.session_state.feynman_notes)
    