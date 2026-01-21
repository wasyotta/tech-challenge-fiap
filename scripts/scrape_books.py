import re
import time
import csv
from dataclasses import dataclass, asdict
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"
START_URL = urljoin(BASE_URL, "catalogue/page-1.html")
OUT_CSV = "data/books.csv"

HEADERS = {"User-Agent": "Mozilla/5.0 (TechChallengeBot/1.0)"}
RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

@dataclass
class BookRow:
    id: int
    title: str
    price: float
    rating: int
    availability: str
    category: str
    image_url: str
    product_page_url: str

def _get(url: str, retries: int = 3):
    last = None
    for _ in range(retries):
        try:
            r = requests.get(url, headers=HEADERS, timeout=20)
            r.raise_for_status()
            return r.text
        except Exception as e:
            last = e
            time.sleep(0.7)
    raise RuntimeError(f"Falha ao baixar {url}: {last}")

def parse_list_page(list_url: str):
    html = _get(list_url)
    soup = BeautifulSoup(html, "lxml")

    links = []
    for a in soup.select("article.product_pod h3 a"):
        links.append(urljoin(list_url, a.get("href", "")))

    next_a = soup.select_one("li.next a")
    next_url = urljoin(list_url, next_a.get("href")) if next_a else None
    return links, next_url

def parse_detail_page(book_url: str):
    html = _get(book_url)
    soup = BeautifulSoup(html, "lxml")

    title = soup.select_one("div.product_main h1").get_text(strip=True)

    price_text = soup.select_one("p.price_color").get_text(strip=True)
    price = float(re.sub(r"[^\d.]", "", price_text))

    rating_p = soup.select_one("p.star-rating")
    rating = 0
    if rating_p:
        for c in rating_p.get("class", []):
            if c in RATING_MAP:
                rating = RATING_MAP[c]
                break

    availability = soup.select_one("p.availability").get_text(" ", strip=True)

    bc = soup.select("ul.breadcrumb li a")
    category = bc[2].get_text(strip=True) if len(bc) >= 3 else "Unknown"

    img_rel = soup.select_one("div.item.active img").get("src", "")
    image_url = urljoin(book_url, img_rel)

    return {
        "title": title,
        "price": price,
        "rating": rating,
        "availability": availability,
        "category": category,
        "image_url": image_url,
        "product_page_url": book_url,
    }

def main():
    rows = []
    url = START_URL
    next_id = 1
    page = 0

    while url:
        page += 1
        print(f"[PAGE {page}] {url}")
        book_links, url = parse_list_page(url)

        for link in book_links:
            d = parse_detail_page(link)
            rows.append(BookRow(
                id=next_id,
                title=d["title"],
                price=d["price"],
                rating=d["rating"],
                availability=d["availability"],
                category=d["category"],
                image_url=d["image_url"],
                product_page_url=d["product_page_url"],
            ))
            next_id += 1

        time.sleep(0.05)

    print(f"Total: {len(rows)} livros")

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        for r in rows:
            writer.writerow(asdict(r))

    print(f"CSV gerado: {OUT_CSV}")

if __name__ == "__main__":
    main()
