from langchain_mongodb.vectorstores import MongoDBAtlasVectorSearch
from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
import os
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Optional, Type
from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

MONGODB_ATLAS_CLUSTER_URI = os.getenv('MONGO_URL')
DB_NAME = "socraites"
COLLECTION_NAME = "embeddings"
ATLAS_VECTOR_SEARCH_INDEX_NAME = "vector_index"

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# initialize MongoDB python client
client = MongoClient(MONGODB_ATLAS_CLUSTER_URI)

MONGODB_COLLECTION = client[DB_NAME][COLLECTION_NAME]

vector_store = MongoDBAtlasVectorSearch(
    collection=MONGODB_COLLECTION,
    embedding=embeddings,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
    relevance_score_fn="cosine",
)

retriever = vector_store.as_retriever(search_kwargs={'k': 10})

model = ChatOpenAI(model='gpt-4o')

prompt = PromptTemplate.from_template(
    """
    You are being provided with context about a specific user question. You need to answer the user question in a maximum of 2 sentences and provide details of the Source and the page number from where you generated the answered so that the user can go there to learn more.
    Always credit the answer to the Author.
    Always include the actual URL and page number where the user can go to learn more.
    If you don't know, just say 'i don't know'.
    Context: {context}
    Question: {question}
    Answer:
    """
)

def format_docs(docs) -> str:
    data = ''
    for doc in docs:
        source = doc.metadata['source']
        author = doc.metadata['author']
        page_number = doc.metadata['page']
        data += f'Source URL: {source}\nAuthor: {author}\nPage Number: {str(page_number)}'
        data += "\n===================================================================\n"
        data += f"{doc.page_content}\n\n"
    return data

chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

class RAG_Input(BaseModel):
    query: str = Field(description="the question to be answered")

class RAGTool(BaseTool):
    name: str = 'RAGTool'
    description: str = "This tool should be used when a question's answer has to be looked up"
    args_schema: Type[BaseModel] = RAG_Input

    def _run(
        self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        return chain.invoke(query)

rag_tools = [RAGTool()]