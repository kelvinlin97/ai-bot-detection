# preprocess.py
import json
import pandas as pd
import re
from pathlib import Path

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.strip()

def load_and_preprocess(json_path):
    with open(json_path) as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    df["clean_text"] = df["text"].apply(clean_text)
    df["word_count"] = df["clean_text"].apply(lambda x: len(x.split()))
    df["unique_vocab_ratio"] = df["clean_text"].apply(lambda x: len(set(x.split())) / max(1, len(x.split())))
    return df

if __name__ == "__main__":
    root = Path("data/")
    for platform in ["twitter", "reddit", "github"]:
        path = root / platform / ("tweets.json" if platform == "twitter" else "posts.json" if platform == "reddit" else "issues.json")
        df = load_and_preprocess(path)
        print(f"\nSample from {platform}:")
        print(df[["user_id", "word_count", "unique_vocab_ratio"]].head())
