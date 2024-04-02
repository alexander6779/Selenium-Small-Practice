# Scraping Temperatures with Selenium

This is a small project where Selenium is used to collect temperature data from a weather forecast webpage. In this case, [tutiempo.net](https://www.tutiempo.net/las-palmas-de-gran-canaria.html?) has been chosen as the data source for demonstration. The project focuses on automating the data collection process using Selenium WebDriver in Python.

## Requirements

- Python 3.x
- Selenium WebDriver
- A compatible web browser (e.g., Chrome, Firefox, etc.)
- Python dependencies (can be installed using `pip`):

## Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/tu-usuario/scraping-temperaturas-selenium.git
```

2. Install Python dependencies:

```bash
pip install openpyxl
pip install pandas
pip install selenium
```
Remember to install the web driver, check the selenium library for more info: https://selenium-python.readthedocs.io/installation.html

3. Run the Python script to obtain temperatures:

```bash
python scraping_temperaturas.py
```

## About the Project

This project aims to demonstrate how to automate data collection using Selenium WebDriver. The scraping_temperatures.py script opens a weather forecast webpage, extracts temperatures for different days, and prints them to the console.

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements or fixes.

## Legal Disclaimer

This project is provided for educational and demonstration purposes only. Web scraping may be subject to legal restrictions and terms of service. Be sure to review and comply with the terms of use of the website you are scraping.