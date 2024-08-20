import requests

BASE = 'http://localhost:5000'

# Add Movie
response = requests.put(f'{BASE}/movie/The Matrix', json={
    'name': 'The Matrix',
    'rate': 10,
    'ranking': 1
})
print(response.json())

# Get Movie
response = requests.get(f'{BASE}/movie/The Matrix')
print(response.json())