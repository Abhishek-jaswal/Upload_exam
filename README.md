# Web Scraper - Python Data Extraction Tool

A Python-based web scraping tool for automated data extraction from websites, with built-in validation, normalization, and export to CSV/JSON formats.

## 🚀 Features

- **Multi-page scraping** - Automatically iterate through paginated content
- **Data validation** - Built-in checks for data consistency and accuracy
- **Multiple export formats** - Save results as CSV or JSON
- **Clean data output** - Normalized and structured datasets ready for analysis
- **Error handling** - Robust error management for reliable extraction

## 🛠️ Tech Stack

- **Python 3.x**
- **BeautifulSoup4** - HTML parsing and navigation
- **Requests** - HTTP library for fetching web pages
- **CSV/JSON** - Built-in Python modules for data export

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/python-web-scraper.git
cd python-web-scraper

# Install dependencies
pip install -r requirements.txt
```

## 🎯 Usage

### Basic Example

```python
python scraper_example.py
```

This will:
1. Scrape book data from books.toscrape.com (a legal practice website)
2. Extract titles, prices, ratings, and availability
3. Save results to `books_data.csv` and `books_data.json`

### Sample Output

```
📚 Sample Results:
------------------------------------------------------------
  Title    : A Light in the Attic
  Price    : £51.77
  Rating   : ⭐⭐⭐⭐ (4/5)
  Stock    : In stock
------------------------------------------------------------
  Title    : Sapiens: A Brief History of Humankind
  Price    : £54.23
  Rating   : ⭐⭐⭐⭐⭐ (5/5)
  Stock    : In stock
------------------------------------------------------------

✅ Total scraped: 60 books
✅ Saved to books_data.csv and books_data.json
```

## 📂 Project Structure

```
python-web-scraper/
├── scraper_example.py      # Main scraping script
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
├── books_data.csv          # Output: CSV format
└── books_data.json         # Output: JSON format
```

## 🔧 How It Works

1. **HTTP Request** - Sends GET request to target URL
2. **HTML Parsing** - BeautifulSoup parses the response HTML
3. **Data Extraction** - Finds specific elements using CSS selectors
4. **Data Processing** - Cleans, validates, and normalizes extracted data
5. **Export** - Saves structured data to CSV/JSON files

## 📊 Code Example

```python
import requests
from bs4 import BeautifulSoup

# Fetch the webpage
response = requests.get("http://books.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")

# Extract data
books = soup.find_all("article", class_="product_pod")
for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text
    print(f"{title} - {price}")
```

## ⚙️ Configuration

Modify the following parameters in `scraper_example.py`:

```python
num_pages = 3        # Number of pages to scrape
BASE_URL = "..."     # Target website URL
```

## 🎓 Use Cases

- **E-commerce price monitoring** - Track product prices across websites
- **Data aggregation** - Collect information from multiple sources
- **Market research** - Gather competitive intelligence
- **Content collection** - Build datasets for analysis or machine learning

## ⚠️ Legal & Ethical Considerations

- Always check `robots.txt` before scraping
- Respect rate limits and don't overload servers
- Only scrape publicly available data
- Review website terms of service
- This project uses `books.toscrape.com` - a site specifically built for scraping practice

## 📝 Requirements

```txt
requests>=2.31.0
beautifulsoup4>=4.12.0
```

## 🚧 Future Enhancements

- [ ] Add Selenium support for JavaScript-heavy sites
- [ ] Implement proxy rotation
- [ ] Add rate limiting and delays
- [ ] Support for more export formats (Excel, SQLite)
- [ ] Concurrent scraping with threading/async

## 👨‍💻 Author

**Abhishek Jaswal**
- Full-Stack Developer
- Location: Dharamshala, Himachal Pradesh, India
- Email: abhignitejaswal@gmail.com
- GitHub: [yourusername](https://github.com/Abhishek-jaswal)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/abhishekjaswall)


---

⭐ If you found this project helpful, please give it a star!