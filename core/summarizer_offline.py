import nltk
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def _ensure_nltk():
    try:
        nltk.find('tokenizers/punkt')
        nltk.find('tokenizers/punkt_tab')
    except LookupError:
        nltk.download('punkt')
        nltk.download('punkt_tab')

def summarize_text(text, num_sentences=3):
    _ensure_nltk()

    if not text.strip():
        return "No Text to Summarize"

    sentences = nltk.sent_tokenize(text)
    if len(sentences) <= num_sentences :
        return text


    vectorizer = TfidfVectorizer()
    sentence_vectors = vectorizer.fit_transform(sentences)


    similarity_matrix = cosine_similarity(sentence_vectors)
    graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(graph)

    ranked = sorted(
        ((scores[i], s) for i, s in enumerate(sentences)),
        reverse = True
    )

    summary = " ".join([s for _, s in ranked[:num_sentences]])
    return summary

if __name__ == "__main__":
    sample = """
    Photosynthesis is a process used by plants and other organisms
    to convert light energy into chemical energy.
    """
    print(summarize_text(sample))

