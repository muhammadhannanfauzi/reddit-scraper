import requests

url = "https://www.reddit.com/r/malaysia/.json"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
data = response.json()

for post in data["data"]["children"]:
    title = post["data"]["title"]
    print(title)