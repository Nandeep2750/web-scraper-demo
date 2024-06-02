# Web Scraping Project

This project is designed to scrape product names from multiple pages of a website using Selenium and BeautifulSoup, and then store the extracted data in a CSV file. The project involves navigating through the website's pages, extracting product names from each page, and saving the results in a structured format.

## Prerequisites

Before running the script, ensure you have the following installed:

1. Python 3.x
2. Selenium
3. BeautifulSoup
4. Pandas
5. ChromeDriver

You can install the required Python packages using `pip`:

`pip install selenium beautifulsoup4 pandas`

You also need to download ChromeDriver and ensure it is available in your PATH or specify its location in the script.

## Setup

1. ChromeDriver: Download the appropriate version of ChromeDriver from here. Make sure it matches the version of Chrome installed on your machine.

2. Project Directory: Place the `web_scraping.py` script in your project directory.

## Script Overview

The script performs the following tasks:

1. Initialize WebDriver: Sets up the Selenium WebDriver using Chrome.
2. Navigate Pages: Loops through each page of the website to scrape data.
3. Extract Data: Uses BeautifulSoup to parse the HTML content and extract product names.
4. Store Data: Saves the extracted product names in a CSV file using Pandas.
5. Close WebDriver: Closes the Selenium WebDriver.

## Running the Script

To run the script, execute the following command in your terminal or command prompt:

`python web_scraping.py`

## Output

The script will generate a CSV file named `names.csv` in the same directory as the script. This file will contain the product names extracted from the website.

## Troubleshooting

1. ChromeDriver Error: Ensure that the version of ChromeDriver matches your installed Chrome browser version.
2. Network Issues: Check your internet connection if the script fails to load the web pages.
3. Changes in Website Structure: If the website's HTML structure changes, you may need to update the parsing logic in the script accordingly.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- [Pandas](https://pandas.pydata.org/)
