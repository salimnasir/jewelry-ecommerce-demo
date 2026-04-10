import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

products = []

for item in soup.select(".product"):
    name = item.select_one(".product-name").text
    price = item.select_one(".price").text
    
    products.append({
        "name": name,
        "price": price
    })

print(products)
