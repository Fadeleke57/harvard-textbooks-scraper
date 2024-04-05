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

def find_table(driver):
    url = 'https://view-awesome-table.com/-MGtjZNWCJ2MVVaoZ7cr/view' #root firebase url for the table
    driver.get(url)
    driver.maximize_window()
    sleep(5)

    table = driver.find_element_by_xpath('//*[@id="chart1"]/div/div[1]/table')
    data = []
    rows = table.find_elements_by_tag_name('tr')
    for row in rows:
        cells = row.find_elements_by_tag_name('td')
        row_data = [cell.text for cell in cells]
        data.append(row_data)

    driver.quit()
    return data

driver = create_webdriver_instance()
data = find_table(driver)
df = pd.DataFrame(data)
print(df)