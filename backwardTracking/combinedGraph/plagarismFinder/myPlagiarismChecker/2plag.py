import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sample_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
sample_contents = [open(File).read() for File in sample_files]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(sample_contents)
s_vectors = list(zip(sample_files, vectors))

def check_plagiarism():
    results = set()
    global s_vectors
    for i, (sample_a, text_vector_a) in enumerate(s_vectors):
        new_vectors = s_vectors.copy()
        del new_vectors[i]
        for sample_b, text_vector_b in new_vectors:
            sim_score = cosine_similarity(text_vector_a, text_vector_b)[0][0]
            if sim_score > 0.7:  # threshold as needed
                common_text = set(sample_contents[i].split()) & set(sample_contents[sample_files.index(sample_b)].split())
                if common_text:
                    results.add((sample_a, sample_b, sim_score, frozenset(common_text)))
    return results

for data in check_plagiarism():
    sample_a, sample_b, sim_score, common_text = data
    print(f"Similarity between {sample_a} and {sample_b}: {sim_score}")
    print("Common Text:")
    #print(" ".join(common_text))
    for text in common_text:
        print(text)
    print("\n")

