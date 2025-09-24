# NHL Teams Stats Scraper

This repository contains a Python web scraper that collects **NHL team statistics** from [scrapethissite.com](https://www.scrapethissite.com/pages/forms/)  
The scraper automatically scans all pages and saves the results in CSV format.

## Features
- HTML parsing with "requests" and "BeautifulSoup"
- Automatic pagination processing
- Saves structured data (team name, year, wins, losses, etc.) in CSV format
- Minimal dependencies, easy to run


## Project Structure
```
NHL-Teams-Stats-Scraper/
├── src/ 
│   └── main.py # main scraper script
├── output/ 
│   └── teams_stats.csv # CSV file with scraped data 
├── GIF/
│   └── demo.gif # optional demo animation
├── .gitignore
├── requirements.txt # dependencies 
└── README.md # project description
```

## Installation
```bash
# The repository
git clone https://github.com/<your-username>/NHL-Teams-Stats-Scraper.git
cd NHL-Teams-Stats-Scraper

# Install dependencies
pip install -r requirements.txt

# Run the scraper
python src/main.py
```

## Demo.gif
![Demo_GIF](https://github.com/Zhasulan-Agybay/NHL-Teams-Stats-Scraper/blob/main/NHL%20Teams%20Stats%20Scraper/GIF/demo.gif)

#### 👨💻 About This Project

Hi, my name is Zhasulan Agybay and this is my web scraping project. It demonstrates how to scrape tabular data from a paginated website and save it in a structured format. You can check out my other projects on GitHub.


## ⚖️ License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
