Amazon Self-Help Book Scraper
This Python script uses Selenium and Google Gemini AI to scrape a public Amazon book list and filter out self-help books automatically.

Features
Scrapes book titles and authors from a specified Amazon list.
Uses Gemini AI to identify self-help books.
Outputs results to a text file.
Requirements
Python 3.8+
Google Chrome
ChromeDriver
Environment variables: API_KEY (Google Gemini API key)
Usage
Clone the repository.
Install dependencies:
Set your Gemini API key in a .env file:
Run the script:
Notes
The script runs Chrome in headless mode.
Output is saved to self-help-books.txt.
