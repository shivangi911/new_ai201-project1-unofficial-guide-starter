# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

UMass Amherst CS professor and course reviews. Students often rely on scattered information from Reddit discussions, Rate My Professor reviews, and informal student recommendations when selecting courses and professors. Official university resources provide course descriptions and instructor names but do not capture student experiences such as workload, teaching quality, exam difficulty, grading style, and professor accessibility.

---

## Document Sources

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | CS187 Reviews | Text file | documents/cs187_reviews.txt |
| 2 | CS220 Reviews | Text file | documents/cs220_reviews.txt |
| 3 | CS250 Reviews | Text file | documents/cs250_reviews.txt |
| 4 | CS311 Reviews | Text file | documents/cs311_reviews.txt |
| 5 | Professor Reviews 1 | Text file | documents/professor_reviews_1.txt |
| 6 | Professor Reviews 2 | Text file | documents/professor_reviews_2.txt |
| 7 | Reddit Easy Courses | Text file | documents/reddit_easy_courses.txt |
| 8 | Reddit Hard Courses | Text file | documents/reddit_hard_courses.txt |
| 9 | Reddit Best Professors | Text file | documents/reddit_best_professors.txt |
| 10 | Reddit CS Advice | Text file | documents/reddit_cs_advice.txt |

---

## Chunking Strategy

**Chunk size:** 500 characters

**Overlap:** 100 characters

**Why these choices fit your documents:**

Most documents consist of short reviews and student comments. A 500-character chunk preserves complete opinions while remaining focused on a single topic. A 100-character overlap helps prevent useful information from being split across chunk boundaries.

**Final chunk count:** 11

---

## Embedding Model

**Model used:**

all-MiniLM-L6-v2

**Production tradeoff reflection:**

I selected all-MiniLM-L6-v2 because it is lightweight, fast, free, and runs locally. For production use, I would consider retrieval accuracy, multilingual support, latency, context length, and infrastructure cost. Larger models may improve semantic understanding but would increase resource requirements.
---

## Grounded Generation

**Question that failed:**

What do students say about biology courses?

**What the system returned:**

It stated that insufficient information was available.

**Root cause (tied to a specific pipeline stage):**

The retrieval stage could not find relevant chunks because the document collection only contains computer science course reviews.

**What you would change to fix it:**

Expand the document collection to include reviews from additional academic departments.

---

## Evaluation Report

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What do students say about CS220 workload? | Moderate to high workload | Correctly summarized workload and project deadlines | Relevant | Accurate |
| 2 | Which courses are considered difficult? | CS250 and CS311 | Correctly identified CS250 and CS311 | Relevant | Accurate |
| 3 | Which courses are beginner friendly? | CS187 and CS220 | Correctly identified beginner-friendly courses | Relevant | Accurate |
| 4 | Which professor is most recommended? | Professor A | Correctly identified Professor A | Relevant | Accurate |
| 5 | What do students say about biology courses? | No information available | Returned insufficient information response | Relevant | Accurate |

---

## Failure Case Analysis

**Question that failed:**

What do students say about biology courses?

**What the system returned:**

It stated that insufficient information was available.

**Root cause (tied to a specific pipeline stage):**

The retrieval stage could not find relevant chunks because the document collection only contains computer science course reviews.

**What you would change to fix it:**

Expand the document collection to include reviews from additional academic departments.

---

## Spec Reflection

**One way the spec helped you during implementation:**

The planning document helped define the chunking strategy, retrieval approach, and evaluation questions before implementation. Having these decisions documented made it easier to build the pipeline step by step.

**One way your implementation diverged from the spec, and why:**

The original plan assumed a larger collection of reviews. Due to time constraints, I used a smaller set of curated text documents while still maintaining the required retrieval and generation workflow.

---

## AI Usage

**Instance 1**

* **What I gave the AI:** I asked questions about how a Retrieval-Augmented Generation (RAG) system works, including embeddings, vector databases, semantic search, and how retrieved documents are used during answer generation.
* **What it produced:** It explained the role of sentence-transformer embeddings, ChromaDB for vector storage, and the retrieval workflow used in a RAG pipeline.
* **What I changed or overrode:** I applied those concepts to my own project by using the all-MiniLM-L6-v2 embedding model, ChromaDB, and my collection of UMass CS review documents. I also verified retrieval quality by examining the returned chunks for my evaluation questions.

**Instance 2**

* **What I gave the AI:** I asked for help debugging issues encountered during development, including creating and activating a virtual environment, configuring the Groq API key, resolving GitHub authentication errors during git push, and connecting the retrieval pipeline to the Gradio interface.
* **What it produced:** It suggested troubleshooting steps, configuration changes, and explanations of the error messages.
* **What I changed or overrode:** I tested the proposed fixes, selected the solutions that worked in my development environment, and verified the final behavior by successfully running the application, retrieving relevant documents, generating answers, and pushing the completed project to GitHub.

