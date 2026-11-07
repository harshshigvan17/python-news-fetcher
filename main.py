import requests
import os

api_key = os.getenv("NEWS_API_KEY")
while True:
    query=input("what type of news are you interested in or (enter quit to exit):-")
    if query == "quit":
        break
    url=f"https://newsapi.org/v2/everything?q={query}&language=en&from=2026-10-07&sortBy=publishedAt&apiKey={api_key}"
    r=requests.get(url)
    news=r.json()

    if "articles" in news :

        for article in news["articles"]:
            print("-------------------------")
            print(article.get("title"))
            print(article.get("description"))
            print("-------------------------")
    else:
        print("No article found for your query. Please try again!")