import os
import chromadb
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer

load_dotenv()

model = SentenceTransformer("all-MiniLM-L6-v2")

chroma_client = chromadb.PersistentClient(path="chroma_db")
collection = chroma_client.get_or_create_collection(name="umass_cs_reviews")

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def retrieve(query, top_k=5):
    query_embedding = model.encode(query).tolist()

    return collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )


def ask(question):
    results = retrieve(question)

    contexts = results["documents"][0]
    metadatas = results["metadatas"][0]

    context_text = ""
    sources = []

    for i, chunk in enumerate(contexts):
        source = metadatas[i]["source"]
        sources.append(source)
        context_text += f"\nSource: {source}\nContent: {chunk}\n"

    prompt = f"""
Answer the question using only the information in the provided context.

If the context does not contain enough information, say:
"I don't have enough information to answer that based on the documents."

Always include source names in your answer.

Context:
{context_text}

Question:
{question}
"""

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    answer = response.choices[0].message.content

    return {
        "answer": answer,
        "sources": list(set(sources))
    }


if __name__ == "__main__":
    question = "What do students say about CS220 workload?"
    result = ask(question)

    print("QUESTION:", question)
    print("\nANSWER:")
    print(result["answer"])

    print("\nSOURCES:")
    for source in result["sources"]:
        print("-", source)