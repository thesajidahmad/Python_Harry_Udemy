# 5. Modules and Pip – Using External Libraries

# Install and import the requests module (if available) and use it to fetch data from "https://api.github.com" .

import requests

x = requests.get("https://api.github.com")

y = x.text

print(x.json())
# print(y)