import requests
import json
import time

subreddit = "malaysia"
base_url = f"https://www.reddit.com/r/{subreddit}/.json"
headers = {"User-Agent": "Mozilla/5.0"}

results = []
after = None  


for i in range(10):
    
    url = base_url if after is None else f"{base_url}?after={after}"
    print(f"🔎 Scraping page {i+1}...")

    response = requests.get(url, headers=headers)
    data = response.json()

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

    
    after = data["data"]["after"]

    
    if after is None:
        break

   
    time.sleep(2)



with open("output.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"✅ Done! {len(results)} posts with images saved in output.json")