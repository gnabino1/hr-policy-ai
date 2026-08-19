""" Step 3: Create embeddings for the document chunks using the Jina Embeddings model. """
from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config
from hr_assistant.logger import get_logger

logger= get_logger(__name__)
def get_embeddings_model():
    """ Return a Jina Embeddings Model. 
        Reads JINA_API_KEY from the environment."""
    logger.info("Initializing embedding model %s", config.EMBEDDING_MODEL_NAME)
    return  JinaEmbeddings(model_name= config.EMBEDDING_MODEL_NAME)

