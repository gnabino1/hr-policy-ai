""" Step 6: Connect to the LLM ( the "brain" of the assistant)"""
from langchain_groq import ChatGroq
from hr_assistant import config
from hr_assistant.logger import get_logger
logger= get_logger(__name__)
def get_llm():
    """ Return a ChatGroq LLM Model. 
        Reads GROQ_API_KEY from the environment."""
    logger.info("Loading LLM Model %s", config.LLM_MODEL_NAME)
    return ChatGroq(model_name=config.LLM_MODEL_NAME, temperature=0)