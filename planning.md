# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->

I chose UMass Amherst CS professor and course reviews. Students often rely on scattered information from Reddit discussions, Rate My Professor reviews, and informal student recommendations when selecting courses and professors. Official university websites provide course descriptions but do not capture student experiences such as workload, teaching quality, exam difficulty, grading style, and helpfulness. This system makes that information searchable and easier to access.

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | CS187 Reviews | Student reviews and opinions about CS187 | documents/cs187_reviews.txt |
| 2 | CS220 Reviews | Student reviews and opinions about CS220 | documents/cs220_reviews.txt |
| 3 | CS250 Reviews | Student reviews and opinions about CS250 | documents/cs250_reviews.txt |
| 4 | CS311 Reviews | Student reviews and opinions about CS311 | documents/cs311_reviews.txt |
| 5 | Professor Reviews 1 | Student comments about a CS professor | documents/professor_reviews_1.txt |
| 6 | Professor Reviews 2 | Student comments about a CS professor | documents/professor_reviews_2.txt |
| 7 | Reddit Thread 1 | Discussion about easiest CS courses | documents/reddit_easy_courses.txt |
| 8 | Reddit Thread 2 | Discussion about difficult CS courses | documents/reddit_hard_courses.txt |
| 9 | Reddit Thread 3 | Discussion about best professors | documents/reddit_best_professors.txt |
| 10 | Reddit Thread 4 | General UMass CS advice | documents/reddit_cs_advice.txt |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:** 500 characters

**Overlap:** 100 characters

**Reasoning:** Most of my documents consist of student reviews, Reddit discussions, and course feedback. A chunk size of 500 characters is large enough to preserve complete opinions and recommendations while remaining focused on a single topic. A 100-character overlap helps prevent important information from being split across chunk boundaries.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:** all-MiniLM-L6-v2

**Top-k:** 5

**Production tradeoff reflection:** all-MiniLM-L6-v2 is lightweight, fast, and free to run locally. In a production system, I would also consider retrieval accuracy, latency, multilingual support, context length, and cost when selecting an embedding model.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What do students say about CS220 workload? | Summary of workload comments found in the documents |
| 2 | Which professor is most frequently recommended? | The professor receiving the most positive feedback |
| 3 | What course do students consider the most difficult? | The course most often described as difficult |
| 4 | What advice do students give for succeeding in CS220? | Recommendations appearing in the reviews |
| 5 | Which courses are considered beginner-friendly? | Courses frequently recommended for beginners |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. Student reviews may be subjective and sometimes contradictory.

2. Important information may be split across chunk boundaries, reducing retrieval quality.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

     ```mermaid
graph LR
A[Documents] --> B[Ingestion and Cleaning]
B --> C[Chunking]
C --> D[Embeddings: all-MiniLM-L6-v2]
D --> E[ChromaDB]
E --> F[Retrieval Top-K]
F --> G[Groq LLM]
G --> H[Answer + Sources]
```

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**

I will use ChatGPT to help implement document loading, cleaning, and chunking. I will verify the generated code by inspecting sample chunks.

**Milestone 4 — Embedding and retrieval:**

I will use ChatGPT to help generate code for creating embeddings using all-MiniLM-L6-v2 and storing them in ChromaDB. I will verify retrieval quality using evaluation questions.

**Milestone 5 — Generation and interface:**

I will use ChatGPT to help integrate Groq with the retrieval pipeline and build a Gradio interface. I will verify that answers are generated only from retrieved context and include source attribution.
