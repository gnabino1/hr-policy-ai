""" Step 2: Split the documents into smaller chunks for better processing. """
from langchain_text_splitters import RecursiveCharacterTextSplitter
from hr_assistant import config
from hr_assistant.logger import get_logger

logger= get_logger(__name__)
def split_into_chunks(documents):
    """ Split the documents into smaller chunks for better processing. Returns a list of document chunks. """
    logger.info("Splitting using recursive character text splitter")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
        length_function=len,
    )
    chunks = text_splitter.split_documents(documents)
    logger.info("Chunk completed: %d", len(chunks))
    return chunks