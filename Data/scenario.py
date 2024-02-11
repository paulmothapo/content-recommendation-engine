import pandas as pd
import random

def generate_scenario(content_data, num_interactions):
    interactions = random.sample(list(content_data['content_id']), num_interactions)
    interaction_history = content_data.loc[content_data['content_id'].isin(interactions)]

    client_preferences = {
        'industries': list(set(interaction_history['industry'])),
        'capabilities': list(set(cap for cap_list in interaction_history['capabilities'] for cap in cap_list))
    }
    
    recommendations = content_data[
        content_data['industry'].isin(client_preferences['industries']) |
        content_data['capabilities'].apply(lambda x: any(cap in x for cap in client_preferences['capabilities']))
    ].sample(n=5)  
    
    return client_preferences, recommendations

content_data = pd.read_csv('data/content_data.csv')

client_preferences, recommendations = generate_scenario(content_data, num_interactions=10)

print("Client Preferences:")
print(client_preferences)
print("\nRecommendations:")
print(recommendations)


recommendations.to_csv('data/recommendations.csv', index=False)
print("\nRecommendations saved to 'recommendations.csv'.")
