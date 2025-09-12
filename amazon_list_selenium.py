from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from Driver import DriverActions
import os
from dotenv import load_dotenv
import google.generativeai as gemini
import ast

# Set up the Gemini Model
load_dotenv()
google_api_key = os.getenv('API_KEY')
gemini.configure(api_key=google_api_key)
model = gemini.GenerativeModel(model_name="gemini-2.5-flash-lite")

# Set up the Chrome Driver
chrome_binary_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary_path
options.add_argument("--headless")
service=ChromeService(ChromeDriverManager().install())
chrome_driver = webdriver.Chrome(service=service, options=options)

def main():
    url = "https://www.amazon.com/shop/johnfish/list/252AOEG17NIJ1?ref_=aip_sf_list_spv_ofs_mixed_d"
    chrome_driver.get(url)
    driver = DriverActions()
    titles = driver.scroll_to_bottom(chrome_driver)
    authors = chrome_driver.find_elements(By.CLASS_NAME, "product-brand-text")

    full_books_list = [(titles[i].text, authors[i].text) for i in range(len(titles))]

    # Use gemini to filter out the self-help books from the list
    contents = f"Filter the self-help books from this list: {full_books_list}. only give the list now don't talk"
    response = model.generate_content(contents=contents)
    self_help_books = ast.literal_eval(response.text)

    file = "self-help-books.txt"
    try:
        books_file = open(file, 'w')
        books_file.writelines(f"{self_help_books[i][0]} by {self_help_books[i][1]}\n" for i in range(len(self_help_books)))
        os.startfile(file)
    finally:
        books_file.close()
    

if __name__ == '__main__':
    main()