import pandas as pd
from time import sleep
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common import exceptions

def create_webdriver_instance(): #works better than chrome for some reason
    options = EdgeOptions()
    options.use_chromium = True
    driver = Edge(options=options)
    return driver

def find_table(driver): #adds table data of each page to dataframe
    print('scraping data...')
    table = driver.find_element_by_xpath('//*[@id="chart1"]/div/div[1]/table')
    rows = table.find_elements_by_tag_name('tr')
    for row in rows:
        cells = row.find_elements_by_tag_name('td')
        row_data = [cell.text for cell in cells]
        data.append(row_data)
    return True

def click_next(driver):
    next_button = driver.find_element_by_xpath('//*[@id="pagination"]/div/div[2]/div')
    next_button.click()

def run():
    url = 'https://view-awesome-table.com/-MGtjZNWCJ2MVVaoZ7cr/view' #root firebase url for the table
    driver = create_webdriver_instance()
    driver.get(url)
    driver.maximize_window()
    sleep(5)

    for _ in range(9): #9 button clicks to get to the end
        find_table(driver) 
        click_next(driver)
    driver.quit()
    print('Scraping complete! Data is located in output.xlsx')
    return True

if __name__ == '__main__':
    data = []
    run()
    df = pd.DataFrame(data)
    df.to_excel("output.xlsx")
    print(df)