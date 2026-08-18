""" Step 6: Connect to the LLM ( the "brain" of the assistant)"""
from langchain_groq import ChatGroq
from hr_assistant import config

def get_llm():
    """ Return a ChatGroq LLM Model. 
        Reads GROQ_API_KEY from the environment."""
    return ChatGroq(model_name=config.LLM_MODEL_NAME, temperature=0)