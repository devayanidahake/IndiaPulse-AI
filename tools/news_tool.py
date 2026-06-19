# Purpose:
#   Collect raw news
#   No AI
#   No summaries
#   No ranking


import requests
import os
from datetime import datetime

NEWS_API_KEY = os.getenv("8159430db19c4a019f3560baec7043d6")

TRUSTED_SOURCES = [
    "reuters",
    "bbc-news"
]

def fetch_global_news():

    url = (
        "https://newsapi.org/v2/top-headlines?"
        f"sources={','.join(TRUSTED_SOURCES)}"
        f"&apiKey={"8159430db19c4a019f3560baec7043d6"}"
    )

    response = requests.get(url, timeout=30)
    print(response.status_code)
    print(response.text)

    data = response.json()

    news = []

    for article in data.get("articles", []):

        news.append(
            {
                "headline": article.get("title"),
                "source": article["source"]["name"],
                "published": article.get("publishedAt"),
                "url": article.get("url"),
                "category": "Global"
            }
        )

    return news