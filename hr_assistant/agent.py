"""Step 7: Build the agent that ties the LLM and search tool together."""
from langchain.agents import create_agent
from hr_assistant.llm import config
from hr_assistant.logger import get_logger
logger = get_logger(__name__)
def create_hr_agent(llm, tools):
    """ Create an agent that uses the LLM and tools to answer questions. """
    logger.info("Loading Agent...")
    return create_agent(
        model=llm,
        tools=tools,
        system_prompt=config.SYSTEM_PROMPT,
    )