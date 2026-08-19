""" Step 1: Load the documents from the HR policy text file. """
from langchain_community.document_loaders import TextLoader
from hr_assistant import config
from hr_assistant.logger import get_logger

logger= get_logger(__name__)
def load_document(file_path: str = config.DATA_FILE_PATH):
    """ Load the documents from the HR policy text file. Returns a list of documents. """
    logger.info("Loading Documents from doc loader: %s", file_path)
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()
    logger.info("Loaded %d documents(s)", len(documents))
    return documents