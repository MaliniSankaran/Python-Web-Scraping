import requests               # to fetch web pages
from bs4 import BeautifulSoup # to parse HTML
import pandas as pd           # to store data in CSV

# 1. URL of the page
url = "https://en.wikipedia.org/wiki/List_of_universities_in_the_United_States"

# 2. Fetch the webpage
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/141.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
html_content = response.text

# 3. Parse HTML
soup = BeautifulSoup(html_content, "html.parser")

# 4. Find all divs containing lists of universities
divs = soup.find_all("div", class_="div-col")

universities = []

# 5. Loop through each div and extract university names
for div in divs:
    for li in div.find_all("li"):
        universities.append(li.get_text(strip=True))

# 6. Print first 10 
print("First 10 universities:", universities[:10])

# 7. Save to CSV
data = pd.DataFrame({"University Name": universities})
data.to_csv("universities_wiki.csv", index=False)
print("Data scraped successfully! Data saved in universities_wiki.csv")

