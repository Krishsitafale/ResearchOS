# Transformers

## Overview

Transformers are deep learning architectures introduced in the 2017 paper **Attention Is All You Need**.

They replaced recurrent architectures for Natural Language Processing by allowing every token in a sentence to attend to every other token simultaneously.

Transformers are the foundation of:

- BERT
- GPT
- Llama
- Gemini
- Claude
- Sentence Transformers

---

# Why Transformers?

Earlier NLP models used RNNs and LSTMs.

These models processed text sequentially.

Problems:

- Slow training
- Poor long-term memory
- Difficult parallelization

Transformers solved these issues using Self-Attention.

---

# Attention

Attention allows each token to determine which other tokens are important for understanding its meaning.

Instead of reading words one after another, every word can interact with every other word.

---

# Self Attention

Self-Attention computes relationships between words in the same sentence.

Example:

"The rover collected soil on Mars."

The word "soil" attends strongly to:

- rover
- collected
- Mars

---

# Query Key Value

Every token produces three vectors:

Query

Represents what information the token is looking for.

Key

Represents what information each token contains.

Value

Represents the information passed to the next layer.

Attention compares Queries with Keys to decide how much of each Value should contribute to the output.

---

# Multi Head Attention

Instead of one attention mechanism, Transformers use multiple attention heads.

Each head can learn different relationships:

- Grammar
- Position
- Subject
- Object
- Temporal information

The outputs are combined into a richer representation.

---

# Feed Forward Network

Each Transformer layer contains a small neural network after the attention mechanism.

This further processes each token independently.

---

# Transformer Encoder

An encoder layer consists of:

- Multi Head Attention
- Add & Normalize
- Feed Forward Network
- Add & Normalize

Multiple encoder layers are stacked to build deep representations.

---

# Sentence Transformers

Standard BERT produces contextual embeddings for tokens.

Sentence Transformers pool these token embeddings into a single fixed-length sentence embedding.

These embeddings are optimized for semantic similarity.

---

# Why Sentence Transformers?

Sentence embeddings enable:

- Semantic Search
- Clustering
- Document Retrieval
- Recommendation Systems
- Retrieval-Augmented Generation (RAG)

---

# Transformers in ResearchOS

ResearchOS uses Sentence Transformers to generate vector embeddings for research paper chunks.

Pipeline:

PDF

↓

Chunking

↓

Sentence Transformer

↓

Embedding

↓

Vector Database

↓

Retriever

↓

LLM

↓

Answer

---

# Advantages

- Parallel computation
- Excellent contextual understanding
- Strong long-range dependency modeling
- State-of-the-art NLP performance

---

# Limitations

- Computationally expensive
- High memory requirements
- Large datasets required for pretraining

---

# Interview Questions

1. Why did Transformers replace RNNs?
2. Explain Self-Attention.
3. What are Query, Key, and Value?
4. What is Multi-Head Attention?
5. Why are Sentence Transformers better for semantic search than BERT?
6. How do Transformers generate embeddings?

---

# Key Takeaways

- Transformers process all tokens simultaneously.
- Self-Attention captures relationships between words.
- Multi-Head Attention learns multiple relationships in parallel.
- Sentence Transformers convert text into dense semantic vectors.
- These vectors power semantic search and Retrieval-Augmented Generation.

---

# Connection to Next Module

Next, we will study Sentence Transformers in depth.

We will learn:

- How embedding models are trained
- Why BERT is not ideal for semantic search
- How Sentence Transformers solve this problem
- How ResearchOS will use them to build a semantic search engine.