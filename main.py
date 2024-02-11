from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from data.process_data import preprocess_text
from multiprocessing import Pool
from pyspark import SparkContext
from pyspark.sql import SparkSession

app = Flask(__name__)

sc = SparkContext("local", "ContentRecommendation")
spark = SparkSession(sc)

content_data = pd.read_csv('data/content_data.csv')

content_data['preprocessed_content'] = content_data['content'].apply(preprocess_text)

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(content_data['preprocessed_content'])

def get_recommendations(query, num_recommendations=5):
    query = preprocess_text(query)

    query_vector = tfidf_vectorizer.transform([query])
    cosine_similarities = sc.parallelize(cosine_similarity(query_vector, tfidf_matrix))

    top_indices = cosine_similarities.flatMap(lambda x: x.argsort()[-num_recommendations:][::-1]).collect()

    recommendations = content_data.iloc[top_indices]

    return recommendations.to_dict(orient='records')

@app.route('/recommend', methods=['POST'])
def recommend_content():
    user_input = request.json['query']
    recommendations = get_recommendations(user_input)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)

sc.stop()
