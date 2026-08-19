""" Wires all the components together into one ready-to-use-agent 
This is the single entry point that main.py(CLI) and app.py(STreamlit)
both call. Each step is handled by  its own module
"""

from hr_assistant import config
from hr_assistant.document_loader import load_document
from hr_assistant.splitter import split_into_chunks
from hr_assistant.llm import get_llm
from hr_assistant.tools import create_search_tool
from hr_assistant.agent import create_hr_agent
from hr_assistant.vector_store import (
    build_vector_store,
    # save_vector_store,
    load_vector_store,
    vector_store_exists,
    get_retriever
)
from hr_assistant.logger import get_logger
from hr_assistant.tracing import check_langsmith_tracing
from hr_assistant.guardrails import REFUSAL_MESSAGE, check_input, check_output

logger= get_logger(__name__)
# def build_vector_store_for_document(file_path: str = config.DATA_FILE_PATH):
#     """ Load + split + embed the document, resuing a saved index if we have one"""
#     if vector_store_exists():
#         logger.info("Found savd vector store on disk. Loading...")
#         load_vector_store()
#     logger.info("No saved vector store found, building one from scratch...")
#     documents= load_document(file_path)
#     chunks= split_into_chunks(documents)
#     logger.info("Loaded '%s' and split it into %d chunks.", file_path, len(chunks))
#     vector_store= build_vector_store(chunks)
#     save_vector_store(vector_store)
#     logger.info("vector store build and saved to disk for next time")
#     return vector_store

# data ingestion
def build_vector_store_for_document(file_path: str = config.DATA_FILE_PATH):
    """ Load + split + embed the document, resuing a Qdrant cloud if we have one"""
    print("vector store exists: %s", vector_store_exists())
    if vector_store_exists():
        logger.info("Found existing QDrant Collection. Loading...")
        return load_vector_store()
    logger.info("No saved vector store found, building one from scratch...")
    documents= load_document(file_path)
    chunks= split_into_chunks(documents)
    logger.info("Loaded '%s' and split it into %d chunks.", file_path, len(chunks))
    vector_store= build_vector_store(chunks)
    logger.info("vector store build and saved to disk for next time")
    return vector_store

# data retrieval
def build_hr_assistant(file_path: str= config.DATA_FILE_PATH):
    """ BUild the Full RAG Agent, ready to answer the questions"""
    logger.info("Building HR Assistant...")
    config.check_api_keys()
    check_langsmith_tracing()
    vector_store= build_vector_store_for_document(file_path)
    retriever= get_retriever(vector_store)
    search_tool= create_search_tool(retriever)
    llm=get_llm()
    agent= create_hr_agent(llm=llm,tools=[search_tool])
    return agent

def ask(agent, question: str)-> str:
    """ Ask the agent a question and return its final answer in plaint text"""
    logger.info("user Question: %s", question)
    # Input guard - to get safe inputs
    input_is_safe, _= check_input(question)
    if not input_is_safe:
        return REFUSAL_MESSAGE
    response= agent.invoke({"messages":[{"role":"user", "content": question}]})
    answer= response["messages"][-1].content
    logger.info("Final Answer %s", answer)
    #output guard - to check if agent gives safe input
    ouput_is_safe, _= check_output(answer)
    if not ouput_is_safe:
        return REFUSAL_MESSAGE

    return answer



