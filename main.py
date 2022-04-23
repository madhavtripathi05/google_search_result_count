# Pre-requisites:
# `pip install selenium webdriver-manager pandas`
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Instantiate a Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# read data from csv
# change the name of file here to read different data
file = pd.read_csv('./data.csv')
# search terms extracted from a column, here 'Keywords'
searchTerms = file['Keywords'].to_list()
# list to be populated after the results are found
searchResults = []

# looping over the search terms
for searchTerm in searchTerms:
    try:
        url = 'https://www.google.co.uk/search?q=' + searchTerm
        # load the webpage
        driver.get(url)
        # find the result element from webpage
        resultStats = driver.find_element_by_id('result-stats')
        # removing 'About' and 'Results' from the text
        results = resultStats.text.split(' ')[1]
        # append the results to the list
        searchResults.append(results)
        print(searchTerm + ': ' + results)
    except Exception as e:
        print(e)
# create new data frame with the search results
df = pd.DataFrame({'Keywords': searchTerms, 'Results': searchResults})
# write the data frame to a csv file
df.to_csv('./results.csv', index=False)

# close the browser
driver.quit()
