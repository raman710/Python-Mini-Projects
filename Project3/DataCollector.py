# Automated Data Collector
# Scrapes book data from a website and saves it to a CSV file

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Headers to identify the request as coming from a browser
headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    # Send GET request to the website
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        print("Website connected successfully!")
    else:
        print("Failed to connect.")
        print("Status Code:", response.status_code)
        exit()

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Empty list to store book details
    books = []

    # Find all book containers
    for book in soup.find_all("article", class_="product_pod"):

        # Extract title
        title = book.h3.a["title"]

        # Extract price
        price = book.find("p", class_="price_color").text

        # Extract availability
        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        # Store data in a dictionary
        books.append({
            "Title": title,
            "Price": price,
            "Availability": availability
        })

    # Convert list into DataFrame
    df = pd.DataFrame(books)

    # Display first five records
    print("\nFirst 5 Books:\n")
    print(df.head())

    # Display total number of books
    print("\nTotal Books Scraped:", len(df))

    # Save data into CSV file
    df.to_csv("products.csv", index=False, encoding="utf-8-sig")

    print("\nData saved successfully as 'products.csv'")

except Exception as e:
    print("An error occurred:")
    print(e)