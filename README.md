# Amazon Book Filter with AI

A powerful web application that combines **Selenium Web Scraper** and **Google Gemini AI** to filter books from Amazon based on any custom criteria.

---

## 🚀 Features
- 🌐 **Web Interface**: Clean Flask-based web UI for easy interaction
- 🤖 **AI-Powered Filtering**: Uses Google Gemini AI to filter books based on any criteria
- 📚 **Smart Scraping**: Automatically extracts book titles and authors from Amazon
- 🎯 **Flexible Filtering**: Filter by genre, author, topic, price range, or any custom criteria
- 💾 **Real-time Results**: Instant filtering with results displayed in the browser
- 🔧 **Headless Option**: Runs Chrome in headless mode for server environments

---

## 🛠 Tech Stack
- **Backend**: Python, Flask, Selenium
- **AI**: Google Gemini API
- **Frontend**: HTML, Bootstrap, Jinja2
- **Browser Automation**: ChromeDriver, WebDriver Manager
- **Environment Management**: python-dotenv

---

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Malzuraiqi/Selenium-and-gemini.git
   cd Selenium-and-gemini
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```env
   API_KEY=your_gemini_api_key_here
   ```

4. **Install Chrome** (if not already installed):
   - **Windows**: Download from [Google Chrome](https://www.google.com/chrome/)
   - **Linux**: `sudo apt install google-chrome-stable`
   - **macOS**: `brew install --cask google-chrome`

---

## 🎮 Usage

### Web Application (Recommended)
1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Enter the following**:
   - **Amazon URL**: Any Amazon book search or list URL
   - **Filter Criteria**: Any filtering criteria (genre, author, topic, etc.)
   - **Headless Mode**: Check for server environments

4. **Click "Filter"** to see results instantly

### Example Filter Criteria
- `"self-help books"`
- `"books by Stephen King"`
- `"fantasy novels"`
- `"programming books under $30"`
- `"highly rated psychology books"`
- `"business and leadership books"`

---

## 🔧 Configuration

### Environment Variables
- `API_KEY`: Your Google Gemini API key

### Optional Settings
- Modify `headless` parameter in the web interface for visible browser mode
- Adjust timeout settings in `amazon_list_selenium.py` for slower connections

---

## 🎯 How It Works

1. **URL Input**: User provides an Amazon book search/list URL
2. **Web Scraping**: Selenium scrapes book titles and authors
3. **AI Filtering**: Gemini AI applies the user's custom filter criteria
4. **Results Display**: Filtered books displayed in real-time
5. **Fallback System**: Sample data used if scraping fails

---

## 📝 Notes

- The application includes **fallback sample data** for testing when scraping is unavailable
- **Chrome browser** is required for the scraping functionality
- For best results, use Amazon URLs that display books in a list format
- The AI filtering works with any descriptive criteria in natural language

---

## 🐛 Troubleshooting

### Common Issues
1. **"Chrome binary not found"**: Install Google Chrome
2. **"No results found"**: Try a different Amazon URL or filter criteria
3. **API errors**: Verify your Gemini API key in the `.env` file

### Debug Mode
Run with headless mode disabled to see the browser in action.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/Malzuraiqi/Selenium-and-gemini/issues).

---

## 📞 Support

If you have any questions or run into issues, please open an issue on GitHub.

---

**Happy Filtering!** 🎉
