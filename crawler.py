import requests
import pandas as pd

query = "machine learning"

url = f"https://dblp.org/search/publ/api?q={query}&format=json"

response = requests.get(url)

data = response.json()

papers = data['result']['hits']['hit']

records = []

for paper in papers:

    info = paper['info']

    title = info.get('title', 'Unknown')

    year = info.get('year', 'Unknown')

    authors = info.get('authors', {}).get('author', [])

    author_names = []

    if isinstance(authors, list):
        for a in authors:
            author_names.append(a['text'])

    elif isinstance(authors, dict):
        author_names.append(authors['text'])

    records.append({
        'title': title,
        'year': year,
        'authors': author_names
    })

df = pd.DataFrame(records)

print(df.head())

df.to_csv("data/papers.csv", index=False)

print("Data saved successfully!")