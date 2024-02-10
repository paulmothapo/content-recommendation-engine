from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__)

content_data = pd.read_csv('data/content_data.csv')

def preprocess_data(data):
    return data

def get_recommendations(query, num_recommendations=5):
    query = preprocess_data([query])

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(content_data['content'])

    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_vectorizer.transform(query))
    top_indices = cosine_similarities.argsort().flatten()[-num_recommendations:][::-1]
    recommendations = content_data.iloc[top_indices]

    return recommendations.to_dict(orient='records')


@app.route('/recommend', methods=['POST'])
def recommend_content():
    user_input = request.json['query']
    recommendations = get_recommendations(user_input)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
