import requests
from bs4 import BeautifulSoup

# Step 1: get webpage
url = "https://example.com"
response = requests.get(url, verify=False)

# Step 2: parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: extract title
title = soup.title.text
print("Page title:", title)
