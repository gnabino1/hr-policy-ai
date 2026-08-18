""" Step 2: Split the documents into smaller chunks for better processing. """
from langchain_text_splitters import RecursiveCharacterTextSplitter
from hr_assistant import config

def split_into_chunks(documents):
    """ Split the documents into smaller chunks for better processing. Returns a list of document chunks. """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
        length_function=len,
    )
    chunks = text_splitter.split_documents(documents)
    return chunks