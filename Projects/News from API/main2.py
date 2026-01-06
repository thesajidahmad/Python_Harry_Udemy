import requests

query = input("What type of news are you interested in today? ")
api = "e33a21c39e1f4397b4f03d6b02da7af1"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-02-08&sortBy=publishedAt&apiKey={api}"

print(url)
r =  requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n****************************************\n")