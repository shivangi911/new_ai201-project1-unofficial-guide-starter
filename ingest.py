from pathlib import Path

DOCUMENTS_DIR = "documents"


def load_documents():
    documents = []

    for file in Path(DOCUMENTS_DIR).glob("*.txt"):
        text = file.read_text(encoding="utf-8")

        documents.append(
            {
                "source": file.name,
                "text": text
            }
        )

    return documents


def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


if __name__ == "__main__":
    docs = load_documents()

    print(f"Loaded {len(docs)} documents")

    for doc in docs[:2]:
        print("\nSOURCE:", doc["source"])

        chunks = chunk_text(doc["text"])

        print("Chunks:", len(chunks))
        print(chunks[0])