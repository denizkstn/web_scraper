# B2B Lead Generator & Analyzer 🎯💼

## About The Project
This project is an automated Business-to-Business (B2B) lead generation and filtering tool built with Python. It is designed to scrape business data (specifically web designers and digital agencies) and intelligently analyze their potential needs.

Instead of just extracting raw data, the script includes a dedicated filtering module (`filter_leads.py`) that processes the extracted information to identify prospective clients who might need website development or digital services. The final output is categorized and exported into targeted Excel files.

## Key Features
* **Targeted Web Scraping:** Extracts detailed business information from specific directories and platforms.
* **Smart Filtering & Analysis:** Analyzes raw data to separate "potential buyers" from standard listings.
* **Business Intelligence (BI):** Converts raw web data into actionable, ready-to-call sales leads.
* **Modular Codebase:** Clean and maintainable architecture separating the main scraper (`b2bscraper.py`) and the data processing logic (`filter_leads.py`).

## Built With
* **Language:** Python 3.x
* **Environment:** macOS / Unix, VS Code
* **Output Formats:** `.xlsx`, `.csv`

## How It Works
1. `b2bscraper.py` navigates the target platforms and extracts raw business profiles.
2. The raw data is passed to `filter_leads.py` for text analysis and keyword filtering.
3. Businesses identified as needing web services are flagged and separated.
4. The final categorized datasets are exported directly to Excel formats for the sales/marketing team.

## Disclaimer
*This project was developed for educational purposes, focusing on data analysis and web automation techniques. All operations are designed to respect the target websites' terms of service and `robots.txt` policies.*

---
*Developed by [Deniz Kaştan](https://www.linkedin.com/in/denizkastan)*
