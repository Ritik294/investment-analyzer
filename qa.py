# qa.py

import numpy as np
from summarize import summarize_text_claude
from embedder import embed_text_titan

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def find_best_context(query, chunks, embeddings, return_index=False):
    query_embedding = embed_text_titan(query)[0]

    scores = [
        cosine_similarity(query_embedding, emb)
        for emb in embeddings
    ]

    top_index = int(np.argmax(scores))
    if return_index:
        return chunks[top_index], top_index
    return chunks[top_index]

def answer_question(query, chunks, embeddings):
    context, index = find_best_context(query, chunks, embeddings, return_index=True)

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{query}
"""
    answer = summarize_text_claude(prompt)
    return answer, context, index
