""" Step 1: Load the documents from the HR policy text file. """
from langchain_community.document_loaders import TextLoader
from hr_assistant import config

def load_document(file_path: str = config.DATA_FILE_PATH):
    """ Load the documents from the HR policy text file. Returns a list of documents. """
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()
    return documents