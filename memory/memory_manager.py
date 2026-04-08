from vectorstore.faiss_store import get_vectorstore

def save_memory(text):
    db, _ = get_vectorstore()
    db.add_texts([text])
    db.save_local("faiss_index")


def retrieve_memory(query):
    db, _ = get_vectorstore()
    docs = db.similarity_search(query, k=2)
    return "\n".join([doc.page_content for doc in docs])