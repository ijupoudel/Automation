from email import header
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from login import loginuserzitestaging
import time
import random
import string
import pathlib
import requests
import psycopg2

connection = psycopg2.connect(
    host='34.83.186.91',
    database='koboform',
    user='kobo',
    password='[<]y.<f!zfNh'
)
cur = connection.cursor()
cur.execute('select * from core_site where project_id = 394')

numberofsite = len(cur.fetchall())
print(numberofsite)
driver = webdriver.Chrome('//home/queen/Desktop/naxa/zite-automation/chromedriver') 
driver.maximize_window()
loginuserzitestaging(driver)
header = {
        'Authorization':'token 1f78420bfd4d2fdc9c52851098e3419787a5dbe7'
    }
driver.get("https://zite.zite.io/#/projects/394?tab=reports")
driver.implicitly_wait(5)

ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 5))  
driver.find_element_by_xpath("//span[text()='create new']").click()
driver.find_element_by_name("title").send_keys(str(ran))
driver.find_element_by_xpath("//span[text()='Select']").click()
driver.find_element_by_xpath("//span[text()='Site']").click()
time.sleep(3)
driver.find_element_by_xpath("//span[text()='Continue']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//span[text()='Create']").click()
driver.find_element_by_xpath("//span[text()='Save']").click()

print (driver.current_url)
path = pathlib.PurePath(driver.current_url)
id = path.name
api = "https://zite.zite.io/api/v2/custom-report/report-data/{}".format(id) 
resp = requests.get("{}".format(api),headers=header,)  
test = resp.json()
a = list(test.get("data"))
print(len(a))
if numberofsite == len(a):
    print("test pass")
else:
    print("test failed")