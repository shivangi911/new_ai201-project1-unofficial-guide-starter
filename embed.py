import chromadb
from sentence_transformers import SentenceTransformer
from ingest import load_documents, chunk_text

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="umass_cs_reviews")

documents = load_documents()

chunk_id = 0

for doc in documents:
    chunks = chunk_text(doc["text"])

    for index, chunk in enumerate(chunks):
        embedding = model.encode(chunk).tolist()

        collection.add(
            ids=[str(chunk_id)],
            embeddings=[embedding],
            documents=[chunk],
            metadatas=[{
                "source": doc["source"],
                "chunk_index": index
            }]
        )

        chunk_id += 1

print(f"Stored {chunk_id} chunks in ChromaDB")