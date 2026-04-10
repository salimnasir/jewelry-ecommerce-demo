import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://example.com/shop"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_products(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    products = []

    items = soup.select(".product-item")  # update selector per site

    for item in items:
        try:
            name = item.select_one(".product-title").get_text(strip=True)
        except:
            name = "N/A"

        try:
            price = item.select_one(".price").get_text(strip=True)
        except:
            price = "N/A"

        try:
            image = item.select_one("img")["src"]
        except:
            image = "N/A"

        try:
            link = item.select_one("a")["href"]
        except:
            link = "N/A"

        products.append({
            "name": name,
            "price": price,
            "image": image,
            "link": link
        })

    return products


def save_to_csv(products, filename="products.csv"):
    keys = products[0].keys()

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(products)


if __name__ == "__main__":
    print("Scraping products...")

    data = get_products(BASE_URL)

    if data:
        save_to_csv(data)
        print(f"Saved {len(data)} products to products.csv")
    else:
        print("No products found.")