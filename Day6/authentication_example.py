import requests

url = "https://httpbin.org/basic-auth/user/pass"

response = requests.get(url, auth=("user", "pass"))

print(response.status_code)
print(response.text)

