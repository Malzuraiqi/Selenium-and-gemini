# Amazon Self-Help Book Scraper

This Python script uses **Selenium** and **Google Gemini AI** to scrape a public Amazon book list and automatically filter out self-help books.

---

## 🚀 Features
- 📚 Scrapes **book titles** and **authors** from a specified Amazon list.  
- 🤖 Uses **Gemini AI** to identify self-help books.  
- 📝 Outputs results to a text file.  

---

## 🛠 Requirements
- Python **3.8+**  
- **Google Chrome**  
- **ChromeDriver**  
- Environment variable: `API_KEY` (**Google Gemini API key**)  

---

## ⚙️ Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Malzuraiqi/Selenium-and-gemini.git
   cd Selenium-and-gemini
   ```
   
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your Gemini API key in a .env file:

   ```env
   API_KEY=your_api_key_here
   ```

4. Run the script:

   ```bash
   python scraper.py
   ```

## 📝 Notes

The script runs Chrome in headless mode.

Output is saved to self-help-books.txt.
