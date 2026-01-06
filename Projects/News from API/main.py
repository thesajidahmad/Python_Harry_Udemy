import requests


API_KEY = "e33a21c39e1f4397b4f03d6b02da7af1"
# topic = input("Enter your news topic: ")
# topic = "jio"

url =  f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

r = requests.get(url)

data = r.json()
articles = data["articles"]

for article in articles:
    print(f"Title = {article["title"]}")
    print(f"Description = {article["description"]}")
    print(f"Url = {article["url"]}")
    print("\n***************************************************\n")