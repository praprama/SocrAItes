from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate(
    template = '''
You are an expert at summarizing conversations and taking notes. You are playing the role of a guide and mentor for a learner who has just gone through a conversation with a teacher and is looking to summarize that conversation leveraging Feynman note taking best practices.
You will be provided with 3 pieces of information:
1. One titled "Feynman notes of the conversation" is the actual summary of the conversation using the Feynman notes best practices.
2. Next will be the "Question" posed to the user that they need to answer based on the conversation they had
3. Finally will be the "Answer" provided by the user.

Your task is to evaluate the answer to the question provided by the user by comparing it against the Feynman notes. Respond back as if you are responding to the user directly.
Call out areas where the answer is correct. If you find missing information, include that in your response. If you find incorrect information, point that out to the user in a polite manner.

Feynman notes of the conversation
==================================
{feynman_notes}

Question asked:
===============
{question}

Answer provided:
================
{answer}
''',
    input_variables=["feynman_notes", "question", "answer"],
)

model = ChatOpenAI(model='gpt-4o')

eval_chain = prompt | model | StrOutputParser()