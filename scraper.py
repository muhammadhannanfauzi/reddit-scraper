import requests
import json


url = "https://www.reddit.com/r/malaysia/.json"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
data = response.json()

results = []

for post in data["data"]["children"]:
    post_data = post["data"]
    title = post_data["title"]
    image_url = post_data.get("url_overridden_by_dest")

    
    if image_url and (
        image_url.endswith(".jpg")
        or image_url.endswith(".png")
        or image_url.endswith(".jpeg")
        or image_url.endswith(".gif")
    ):
        results.append({
            "post_title": title,
            "image_url": image_url
        })


with open("output.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Done! Results saved in output.json")