""" Step 5: Wrap the retriver as a tool the agent can call"""

from langchain_core.tools import tool
from hr_assistant.vector_store import get_retriever
from hr_assistant.logger import get_logger
logger= get_logger(__name__)
def create_search_tool(retriever):
    """"  Return a @ tool function that search the HR Policy Document."""
    @tool
    def search_hr_policy(question: str)-> str:
        """ Search the HR Policy Document for the answer to the question. """
        matching_chunks= retriever.invoke(question)
        logger.info("Matching Chunks '%d'", len(matching_chunks))
        return "\n\n".join([chunk.page_content for chunk in matching_chunks])
    
    return search_hr_policy