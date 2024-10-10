from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser, JsonOutputParser
from pydantic import BaseModel, Field, model_validator
from typing import List

class Question(BaseModel):
    section: str = Field(description="The section in the notes the question is supposed to fill up")
    question: str = Field(description="The question to ask the user")

class QuestionList(BaseModel):
    cfu_questions: List[Question] = Field(description="the list of question objects")

parser = PydanticOutputParser(pydantic_object=QuestionList)

prompt = PromptTemplate(
    template = '''
You are an expert at summarizing conversations and taking notes. You are playing the role of a guide and mentor for a learner who has just gone through a conversation with a teacher and is looking to summarize that conversation leveraging Feynman note taking best practices.
You will be provided with a summary of the conversation in the form of Feynman notes below. You need to break the notes up into logical sections and come up with questions to ask the learner so that they can fill up each of the sections based on each question.
You should not provide the notes to the learner. Your job is only to guide the learner in the process of filling up the notes by coming up with the questions.
Your response should be in a JSON format which has a key of 'cfu_questions' whose value is an array. Each element in the array should contain 2 keys 'section' and 'question'.

Feynman notes of the conversation
==================================
{feynman_notes}''',
    input_variables=["feynman_notes"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

model = ChatOpenAI(model='gpt-4o')

cfu_chain = prompt | model | JsonOutputParser()