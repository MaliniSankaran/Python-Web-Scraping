
# Python-Web-Scraping

This repository contains two Python scripts that demonstrate basic web scraping techniques. Each script is standalone and will generate a `.csv` file with the scraped data.

## Setup and Usage

To get started, ensure Python 3 is installed. Then follow these steps:

### 1. Clone the repository

git clone https://github.com/MaliniSankaran/Python-Web-Scraping.git

cd Python-Web-Scraping

### 2. Create and activate a virtual environment

**On Windows:**
  
  `py -3 -m venv venv `
  
  `venv\Scripts\activate `

**On macOS / Linux:**

  `python3 -m venv venv`

  `source venv/bin/activate`

### 3. Install the required libraries
  pip install requests beautifulsoup4 pandas

### 4. Run the scripts
  To run the university list scraper

  `python university_scraper.py`

  To run the Google Scholar scraper

  `python scholar_scraper.py`

## Scripts and Sample Output

### university_scraper.py

This script scrapes a list of universities in the United States from a designated Wikipedia page. It extracts the names of the institutions and saves them into `universities_wiki.csv`.

**Sample Output (first 10 universities):**

`First 10 universities: ['American College Dublin', 'American College of Thessaloniki(ACT)', 'American College of Greece', 'American College of the Mediterranean', 'American InterContinental University', 'American University in Bosnia and Herzegovina', 'American University in Bulgaria', 'The American University in Cairo', 'American University in Dubai', 'American University of Antigua']
Data scraped successfully! Data saved in universities_wiki.csv`

### scholar_scraper.py

This script queries Google Scholar for a specified academic topic (e.g., "Machine Learning"), then parses search results to extract:

- Paper Title
- Authors and Publication Source
- Publication Year

It uses `requests` and `BeautifulSoup` for scraping, `re` for data cleaning and year extraction, and saves the results into `scholar_papers.csv` using `pandas`.

**Sample Output:**

`{'Title': 'Machine learning', 'Authors': 'ZH Zhou - 2021 - books.google.com', 'Year': '2021'}
{'Title': 'Machine learning', 'Authors': 'E Alpaydin - 2021 - books.google.com', 'Year': '2021'}
{'Title': 'Machine learning: Trends, perspectives, and prospects', 'Authors': 'MI Jordan, TM Mitchell\xa0- Science, 2015 - science.org', 'Year': '2015'}
{'Title': 'What is machine learning?', 'Authors': 'I El Naqa, MJ Murphy\xa0- Machine learning in radiation oncology: theory and\xa0…, 2015 - Springer', 'Year': '2015'}
{'Title': 'Machine learning', 'Authors': 'TG Dietterich\xa0- Annual review of computer science, 1990 - engr.oregonstate.edu', 'Year': '1990'}
Google Scholar data scraped! Data saved in scholar_papers.csv`


