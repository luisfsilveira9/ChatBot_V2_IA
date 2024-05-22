from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np

def load_texts(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        texts = f.read().splitlines()
    return texts

def cluster_texts(texts, num_clusters):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)
    
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X)
    
    clusters = kmeans.labels_.tolist()
    return clusters

if __name__ == "__main__":
    texts = load_texts("../data/processed/sample_texts.txt")
    clusters = cluster_texts(texts, num_clusters=5)
    
    with open("../data/processed/texts_with_clusters.tsv", 'w', encoding='utf-8') as f:
        for text, cluster in zip(texts, clusters):
            f.write(f"{text}\t{cluster}\n")
