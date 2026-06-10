from pathlib import Path

DOCUMENTS_DIR = "documents"


def load_documents():
    documents = []

    for file in Path(DOCUMENTS_DIR).glob("*.txt"):
        text = file.read_text(encoding="utf-8")
        text = " ".join(text.split())

        if text.strip():
            documents.append(
                {
                    "source": file.name,
                    "text": text
                }
            )

    return documents


def chunk_text(text, chunk_size=150, overlap=30):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


if __name__ == "__main__":
    docs = load_documents()

    print(f"Loaded {len(docs)} documents")

    total_chunks = 0

    for doc in docs:
        chunks = chunk_text(doc["text"])
        total_chunks += len(chunks)

        print("\nSOURCE:", doc["source"])
        print("Chunks:", len(chunks))
        print("Sample:", chunks[0])

    print("\nTotal chunks:", total_chunks)