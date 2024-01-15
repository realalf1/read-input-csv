import csv
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

# about:profiles -> create new profile -> Root Directory
# C:/Users/Administrator/AppData/Roaming/Mozilla/Firefox/Profiles/4trbl1o3.automation

options = Options()
options.add_argument("-profile")
options.add_argument("C:/Users/Administrator/AppData/Roaming/Mozilla/Firefox/Profiles/4trbl1o3.automation")
driver = webdriver.Firefox(options)
driver.maximize_window()

url = "https://demoqa.com/webtables"

driver.get(url)

driver.implicitly_wait(5)
for i in range(1,4):
    driver.find_element(By.XPATH, (f'//*[@id="delete-record-{i}"]')).click()

with open ("data.csv", "r") as f:
    data = csv.reader(f)
  # assume if first row is not actual data, you need to next then.
    next(data)
    for row in data:
        driver.find_element(By.ID, ('addNewRecordButton')).click() # add
        driver.find_element(By.ID, 'firstName').send_keys(row[0])
        driver.find_element(By.ID, 'lastName').send_keys(row[1])
        driver.find_element(By.ID, 'userEmail').send_keys(row[2])
        driver.find_element(By.ID, 'age').send_keys(row[3])
        driver.find_element(By.ID, 'salary').send_keys(row[4])
        driver.find_element(By.ID, 'department').send_keys(row[5])
        driver.find_element(By.ID, 'submit').click() # submit

# with open("data.csv", "r") as f:
#     data = csv.reader(f)
#     next(data)
#     for i in data:
#         print(i)

time.sleep(3)
driver.quit()
