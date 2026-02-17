import requests
from bs4 import BeautifulSoup
import csv

# ✅ STEP 1 — Visit the website
url = "http://books.toscrape.com/catalogue/page-1.html"
response = requests.get(url)

# ✅ STEP 2 — Read the HTML
soup = BeautifulSoup(response.text, "html.parser")

# ✅ STEP 3 — Find all books on the page
books = soup.find_all("article", class_="product_pod")

# ✅ STEP 4 — Extract data from each book
all_books = []
for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text
    all_books.append({"title": title, "price": price})
    print(f"Found: {title} — {price}")

# ✅ STEP 5 — Save to CSV file
with open("books.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price"])
    writer.writeheader()
    writer.writerows(all_books)

print(f"\n✅ Done! Saved {len(all_books)} books to books.csv")