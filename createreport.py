from email import header
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from login import loginuserzitestaging

import random
import string
import pathlib
import requests


driver = webdriver.Chrome('//home/queen/Desktop/naxa/zite-automation/chromedriver') 
wait = WebDriverWait(driver, 10)
driver.maximize_window()
loginuserzitestaging(driver)
driver.get("https://zite.zite.io/#/projects/394?tab=reports")
driver.implicitly_wait(10)
def casereport():
    global id, column_selected
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 5))  
    driver.find_element_by_xpath("//span[text()='create new']").click()
    driver.find_element_by_name("title").send_keys(str(ran))
    driver.find_element_by_xpath("//span[text()='Select']").click()
    driver.find_element_by_xpath("//span[text()='Case']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//span[text()='Continue']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//span[text()='Metrics']").click()
    driver.find_element_by_xpath("//p[text()='Case Information Details']").click()
    driver.find_element_by_xpath("//p[text()='User Details']").click()
    case = {
        "Number of Submissions in Case",
        "Case Status",
        "Progress",
        "Comments",
        "Last Date Reviewed",
        "Last User to Review",
        "Case History",
        "Reason",
        "Username",
        "Full Name",
        "Phone",
        "Email"
    }
    forminfo = {
        "Details/calculation",
        "Details/PersonalWha/What is your name ?",
        "Details/PersonalWha/What is your age?",
        "Most Recent",
        "Details/PersonalWha/What is your age?",
        "Details/PersonalWha/what is your weight?",
        "Most Recent",
        "Details/PersonalWha/what is your weight?",
        "Details/PersonalWha/What is your gender?",
        "Details/PersonalWha/your date of birth?",
        "Details/Friends details/Each Friend Details/What is your friend name ?",
        "Details/Friends details/Each Friend Details/What is your friend gender?",
        "Details/Friends details/Each Friend Details/What is hisher height?",
        "Most Recent",
        "Details/Friends details/Each Friend Details/What is hisher height?",
        "Details/Friends details/Each Friend Details/when were heshe born?"
    }
    for cases in case:
        driver.find_element_by_xpath("//a[text()='{}']".format(cases)).click()

    driver.find_element_by_xpath("//span[text()='Form Information']").click()
    driver.find_element_by_xpath("//p[text()='Form2.0']").click()
    for questions in forminfo:
        try:
            driver.find_element_by_xpath("//a[text()='{}']".format(questions)).click()
        except:
            driver.find_element_by_xpath("//p[text()='{}']".format(questions)).click()
    column_selected = driver.find_elements_by_xpath("//div[@class='edit-close is-flex is-start']//i[text()='close']")
    print("----------------------------------------------------------------------------------------------------")
    print(len(column_selected))
    driver.find_element_by_xpath("//span[text()='Create']").click()
    driver.find_element_by_xpath("//span[text()='Save']").click()
    driver.implicitly_wait(10)
    print (driver.current_url)
    path = pathlib.PurePath(driver.current_url)
    id = path.name
casereport()

header = {
        'Authorization':'token 1f78420bfd4d2fdc9c52851098e3419787a5dbe7'
    }
api = "https://zite.zite.io/api/v2/custom-report/report-data/{}".format(id)
resp = requests.get("{}".format(api),headers=header,)     
# print(*[api, resp.status_code, resp.json()])
a = list(resp.json().get("header"))
reportheader = len(a)
if len(column_selected)+2 == reportheader:
    print("Test Pass")
    print("All selected columns appears")
else:
    print("Test failed")
    print("All column didn't apper")
