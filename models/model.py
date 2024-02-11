from sklearn.metrics.pairwise import linear_kernel

def get_recommendations(query, tfidf_matrix, tfidf_vectorizer, content_data, num_recommendations=5):
    query_vector = tfidf_vectorizer.transform([query])
    cosine_similarities = linear_kernel(query_vector, tfidf_matrix)
    top_indices = cosine_similarities.argsort().flatten()[-num_recommendations:][::-1]
    recommendations = content_data.iloc[top_indices]
    return recommendations.to_dict(orient='records')
