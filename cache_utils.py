# cache_utils.py

import hashlib
import os
import json
import numpy as np

CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def hash_file(file_path):
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def save_summary(hash_id, summaries):
    with open(f"{CACHE_DIR}/{hash_id}_summary.json", "w", encoding="utf-8") as f:
        json.dump(summaries, f, ensure_ascii=False)

def load_summary(hash_id):
    path = f"{CACHE_DIR}/{hash_id}_summary.json"
    return json.load(open(path, "r", encoding="utf-8")) if os.path.exists(path) else None

def save_embeddings(hash_id, embeddings):
    np.save(f"{CACHE_DIR}/{hash_id}_embed.npy", np.array(embeddings))

def load_embeddings(hash_id):
    path = f"{CACHE_DIR}/{hash_id}_embed.npy"
    return np.load(path, allow_pickle=True).tolist() if os.path.exists(path) else None
