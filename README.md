# Reddit Scraper
This project is a simple Reddit scraper.  
It collects posts from a subreddit, filters only posts with images, saves them into a JSON file (`output.json`), and displays them on a web page (`index.html`).

# How to Use

## 1. Clone the repository
```bash
git clone https://github.com/your-username/reddit-scraper.git
cd reddit-scraper
```

## 2. Install dependencies
```bash
pip install requests
```

## 3. Run the scraper
```bash
python scraper.py
```

## 4. Run a local server (to view results)
```bash
python -m http.server 8000
```
### Then open http://localhost:8000/index.html in your browser
