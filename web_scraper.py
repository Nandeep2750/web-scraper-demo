import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# Set up the webdriver
driver = webdriver.Chrome()

# Create a list to store the results
results = []

# Loop through each page
for page in range(1, 95):  # assuming 94 pages
    # Navigate to the webpage
    driver.get(f'https://sandbox.oxylabs.io/products?page={page}')

    # Get the page source
    content = driver.page_source

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Find all elements with the class "product-card"
    product_cards = soup.find_all(attrs={'class': 'product-card'})

    # Loop through each product card and extract the name
    for card in product_cards:
        name = card.find('h4')
        if name:
            results.append(name.text)

# Create a Pandas DataFrame from the results
df = pd.DataFrame({'Names': results})

# Export the data to a CSV file
df.to_csv('names.csv', index=False, encoding='utf-8')

# Close the webdriver
driver.quit()