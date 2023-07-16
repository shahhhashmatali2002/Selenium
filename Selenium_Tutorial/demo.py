from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import Select
import time

# Set the path to the ChromeDriver executable
chrome_options = Options()
chrome_options.add_argument("chromedriver.exe")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to a website
driver.get("https://www.adamchoi.co.uk/overs/detailed")

# Find an element by its ID and interact with it
element = driver.find_element("xpath",'//label[@analytics-event="All matches"]')
element.click()


def findMatchesDataAllCountry(dropdownItem):
    print('function start....')
    print('getting matches data')
    matches = driver.find_elements(By.TAG_NAME, 'tr')
    # creating array for store data 
    date = []
    home_team = []
    score = []
    away_team = []
    
    print('using loop storing data of each row of column in seperate array....')
    for match in matches:
        date.append(match.find_element("xpath",'./td[1]').text)
        home_team.append(match.find_element("xpath",'./td[2]').text)
        score.append(match.find_element("xpath",'./td[3]').text)
        away_team.append(match.find_element("xpath",'./td[4]').text)
    # driver.quit()


    print(date)
    print(home_team)
    print(score)
    print(away_team)
    

    print('Checking data is in array or array empty...')
    if date and home_team and score and away_team:
        print(f'Now creating csv file and storing data of {dropdownItem} country')
        df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team })
        df.to_csv(f'{dropdownItem}.csv')
        print('Finish and now another continue for another country.....')


dropdown = Select(driver.find_element(By.ID, 'country'))

dropdwonOptions = dropdown.options


for i in dropdwonOptions[9:]:
    if i.text == 'Norway':
        print(f'dropdwon fetching data Start from {i.text}')
        print(i.text)
        dropdown.select_by_visible_text(i.text)
        time.sleep(10)
        print('Now calling function to fetch all data from table....')
        findMatchesDataAllCountry(i.text)




# Close the browser
# driver.quit()