import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

# 1. Define search query 
query = "Machine Learning"
url = f"https://scholar.google.com/scholar?q={query.replace(' ', '+')}"

# 2. Define headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/141.0.0.0 Safari/537.36"
}

# 3. Send HTTP GET request to fetch HTML content
response = requests.get(url, headers=headers)

# Parse the fetched HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# 4. Preparing a list to store paper data
papers = []

# 5. Find the first 5 search results
results = soup.find_all("div", class_="gs_ri")[:5]

# 6. Loop through each result and extract information
for result in results:
    # Extract paper title
    title_tag = result.find("h3", class_="gs_rt")
    title = title_tag.get_text() if title_tag else "N/A"
     
    # Clean title: remove any [XXX] or [XXX][XXX] tags at the start
    title = re.sub(r'^(?:\[[^\]]*\]\s*)+', '', title)

    # Extract authors and publication info (journal, source)
    author_info_tag = result.find("div", class_="gs_a")
    authors_info = author_info_tag.get_text() if author_info_tag else "N/A"

    # Extract year from author info using regex
    year = "N/A"
    # Try to extract year from author info (usually last 4 digits)
    year_match = re.search(r"\b(19|20)\d{2}\b", authors_info)
    if year_match:
        year = year_match.group(0)

    # Append the cleaned data as a dictionary to the list
    papers.append({
        "Title": title,
        "Authors": authors_info,
        "Year": year
    })

# 7. Print result - first 5 papers
for paper in papers:
    print(paper)

# 8. Save to CSV
data = pd.DataFrame(papers)
data.to_csv("scholar_papers.csv", index=False)
print("Google Scholar data scraped! Data saved in scholar_papers.csv")
