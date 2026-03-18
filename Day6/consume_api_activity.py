import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

data = response.json()

print("Status:", response.status_code)
print("Total posts:", len(data))

# Print first post title
print("First post title:", data[0]["title"])
