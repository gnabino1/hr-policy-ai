""" Step 4: Create a vector store for the document chunks using the FAISS vector(old)- moved to QDRANT store. So, we can search thme """
import os
# from langchain_community.vectorstores import FAISS
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from hr_assistant import config
from hr_assistant.embeddings import get_embeddings_model
from hr_assistant.logger import get_logger

logger= get_logger(__name__)

### VECTOR STORE FOR DISK
# def build_vector_store(chunks):
#     """ Embed every chunk and build a searchable FAISS Index in memeory."""
#     embeddings_model= get_embeddings_model()
#     logger.info("Builder vector store...")
#     return FAISS.from_documents(chunks, embeddings_model)

## Save Vector Store to Disk
# def save_vector_store(vector_store, path: str = config.VECTOR_STORE_PATH):
#     """" Save the FAISS Index to disk. SO we don't have to rebuild it every time """
#     logger.info("Saving vector store to '%s'", path )
#     vector_store.save_local(path)

# def load_vector_store(path: str = config.VECTOR_STORE_PATH):
#     """ Load the FAISS Index from disk. """
#     embeddings_model= get_embeddings_model()
#     logger.info("Loading vector store from '%s'", path)
#     return FAISS.load_local(path, embeddings_model, allow_dangerous_deserialization=True)

# def vector_store_exists(path: str = config.VECTOR_STORE_PATH)-> bool:
#     """ Check if the FAISS Index exists on disk. """
#     return os.path.exists(os.path.join(path, "index.faiss"))

### VECTOR STORE FOR QDRANT
def build_vector_store(chunks):
    """ Embed every chunk and build a searchable QDRANT cloud collection."""
    embeddings_model= get_embeddings_model()
    logger.info("Embedding %d chunk(s) into  QDrant COllection", len(chunks))
    vector_store= QdrantVectorStore.from_documents(
        chunks,
        embedding=embeddings_model,
        url= config.QDRANT_URL,
        api_key= config.QDRANT_API_KEY,
        collection_name=config.QDRANT_COLLECTION_NAME
    )
    logger.info("Upload to QDrant Collection %s", config.QDRANT_COLLECTION_NAME)
    return vector_store

def load_vector_store():
    """ Connect to QDrant Clound collection that was already built before"""
    logger.info("Connecting to Qdrant Cloud...")
    embeddings_model= get_embeddings_model()
    return QdrantVectorStore.from_documents(
        embedding=embeddings_model,
        url= config.QDRANT_URL,
        api_key= config.QDRANT_API_KEY,
        collection_name=config.QDRANT_COLLECTION_NAME
    )

def vector_store_exists()-> bool:
    """ Check if Qdrant store already exists"""
    client= QdrantClient(
        url=config.QDRANT_URL,
        api_key=config.QDRANT_API_KEY,

    )
    return client.collection_exists(config.QDRANT_COLLECTION_NAME)


def get_retriever(vector_store, top_k: int = config.TOP_K_RESULTS):
    """ Get a retriever from the FAISS Index. """
    return vector_store.as_retriever(search_kwargs={"k": top_k})