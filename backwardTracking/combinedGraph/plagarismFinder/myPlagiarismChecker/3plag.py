import os
import argparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_files(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    contents = [open(os.path.join(directory, f)).read() for f in files]
    return files, contents

def check_plagiarism(files, contents, threshold=0.7):
    results = set()
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(contents)
    s_vectors = list(zip(files, vectors))

    for i, (sample_a, text_vector_a) in enumerate(s_vectors):
        new_vectors = s_vectors.copy()
        del new_vectors[i]

        for sample_b, text_vector_b in new_vectors:
            sim_score = cosine_similarity(text_vector_a, text_vector_b)[0][0]

            if sim_score > threshold:
                common_text = set(contents[i].split()) & set(contents[files.index(sample_b)].split())

                if common_text:
                    results.add((sample_a, sample_b, sim_score, frozenset(common_text)))

    return results

parser = argparse.ArgumentParser()    
parser.add_argument("output_folder", type=str, help="Output folder name")    
args = parser.parse_args()    

#directory = "./step2-data/onlyRetrievals"
directory = args.output_folder 
sample_files, sample_contents = read_files(directory)

output_file = os.path.join(directory, "commonPatternInMultipleVariants")
with open(output_file, "w") as file:
    for data in check_plagiarism(sample_files, sample_contents):
        sample_a, sample_b, sim_score, common_text = data
        file.write(f"Similarity between {sample_a} and {sample_b}: {sim_score}\n")
        file.write("Common Text:\n")
        for text in common_text:
            file.write(text)
            file.write("\n")
        file.write("\n")

