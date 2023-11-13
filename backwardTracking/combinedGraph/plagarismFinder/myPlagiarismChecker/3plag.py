import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sample_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
sample_contents = [open(File).read() for File in sample_files]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(sample_contents)
s_vectors = list(zip(sample_files, vectors))

def get_first_and_last_common_text(file1, file2):
    words1 = file1.split()
    words2 = file2.split()

    common_words = set(words1) & set(words2)

    if not common_words:
        return None

    first_common_word = min(common_words, key=lambda x: (words1.index(x), words2.index(x)))
    last_common_word = max(common_words, key=lambda x: (words1[::-1].index(x), words2[::-1].index(x)))

    return first_common_word, last_common_word

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
                print("set(sample_contents[i].split()) & set(sample_contents[sample_files.index(sample_b)].split()): ", common_text)
                #one_more = set(sample_contents[i+1].split()) & set(sample_contents[sample_files.index(sample_b)].split())
                #common_text = get_first_and_last_common_text(sample_contents[i], sample_contents[sample_files.index(sample_b)])
                #common_text = list(common_text)
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

