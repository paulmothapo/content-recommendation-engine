import pandas as pd
import random

keywords = [
    'why', 'how', 'tech', 'money', 'finance', 'services', 'AI', 'what', 'to', 'do', 'money', 'crypto', 
    'solar', 'energy', 'The', 'when', 'what', 'time', 'sustain', 'ESG', 'economy', 'business', 'impact', 
    'health', 'education', 'edtech', 'healthcare tech', 'VR', 'many', 'ways', 'more', 'keep', 'moving', 
    'sell', 'market', 'products', 'expensive', 'luxury', 'cheap', 'rise', 'raise', 'improve', 'data', 
    'insights', 'customers', 'strategic', 'management', 'consulting'
]


industries = ['education', 'healthcare', 'energy', 'financial services', 'technology', 'retail']
capabilities = ['sustainability', 'digital transformation', 'customer insights', 'sales & marketing', 'innovation', 'strategy management', 'M&a']

num_content = 100
content_data = {
    'content_id': list(range(1, num_content + 1)),
    'title': [f"{random.choice(keywords)} {random.choice(keywords)} {random.choice(keywords)}" for _ in range(num_content)],
    'content': [f"Content {i}" for i in range(1, num_content + 1)]
}

random.shuffle(industries)
random.shuffle(capabilities)

content_data['industry'] = [random.choice(industries) for _ in range(num_content)]
content_data['capabilities'] = [random.sample(capabilities, random.randint(1, len(capabilities))) for _ in range(num_content)]

df = pd.DataFrame(content_data)

df.to_csv('data/content_data.csv', index=False)

print("content_data.csv has been generated successfully.")
