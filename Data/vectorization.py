from sklearn.feature_extraction.text import TfidfVectorizer

def tfidf_vectorize(data):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(data)
    return tfidf_matrix, tfidf_vectorizer
