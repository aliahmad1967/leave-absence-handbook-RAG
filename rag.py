import requests
import numpy as np
from pathlib import Path

OLLAMA = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text:latest"
CHAT_MODEL = "qwen3.8:latest"

def embed(texts):
    r = requests.post(f"{OLLAMA}/api/embed", json={"model": EMBED_MODEL, "input": texts})
    return np.array(r.json()["embeddings"])


def ask_llm(prompt, history=None):
    if history is None:
        history = []
    r = requests.post(f"{OLLAMA}/api/chat", json={"model": CHAT_MODEL, "stream": False, "messages": history + [{"role": "user", "content": prompt}]})
    return r.json()["message"]["content"]


chunks = []
for file in Path("docs").glob("*.md"):
    chunks =[p.strip() for p in file.read_text(encoding="utf-8").split("\n\n") if p.strip()]


chunk_vectors= embed(chunks)
print(f"indexed {len(chunks)} chunks with shape {chunk_vectors.shape}")

def retrieve(question, k=3):
    q = embed([question])[0]
    scores = chunk_vectors @ q / (np.linalg.norm(chunk_vectors, axis=1) * np.linalg.norm(q))
    return [chunks[i] for i in np.argsort(scores) [ ::- 1][:k]]


while True:
    question = input("Question: ")
    if question.strip() == "":
        break
    context = retrieve(question)
    prompt = f"Answer the question based on the context below. If the question can't be answered based on the context, say 'I don't know'.\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
    answer = ask_llm(prompt)
    print(f"Answer: {answer}")