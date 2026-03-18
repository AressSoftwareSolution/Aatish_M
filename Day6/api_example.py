# import requests

# url = "https://api.github.com"

# response = requests.get(url)

# print(response.status_code)
# print(response.json())


import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(response.status_code)
print(response.json())
