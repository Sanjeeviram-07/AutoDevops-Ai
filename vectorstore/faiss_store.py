from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
def get_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    try:
        db = FAISS.load_local("faiss_index", embeddings)
    except:
        db = FAISS.from_texts(["initial memory"], embeddings)

    return db, embeddings 