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

driver = webdriver.Chrome('//home/queen/Desktop/naxa/zite-automation/chromedriver') 
driver.maximize_window()
loginuserzitestaging(driver)
header = {
        'Authorization':'token 1f78420bfd4d2fdc9c52851098e3419787a5dbe7'
    }
driver.get("https://zite.zite.io/#/projects/416?tab=reports")
driver.implicitly_wait(5)
def createsiterepo():
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 5))  
    driver.find_element_by_xpath("//span[text()='create new']").click()
    driver.find_element_by_name("title").send_keys(str(ran))
    driver.find_element_by_xpath("//span[text()='Select']").click()
    driver.find_element_by_xpath("//span[text()='Site']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//span[text()='Continue']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//span[text()='Metrics']").click()

Po = [
    "Number of Submissions",
    "Submissions Reviewed", 
    "Active Users by Role",
    "Individual Form Metrics",
    "Form2.0"

]
case = [
        "Progress", 
        "Status of Most Recent Submission", 
        "Total Submissions", 
        "Pending Submissions", 
        "Approved Submissions", 
        "Flagged Submissions", 
        "Rejected Submissions", 
        "In Progress Submissions", 
        "Total Reviews", 
        "Submissions Flagged", 
        "Submissions Rejected", 
        "Submissions Approved", 
        "Submissions In Progress", 
        "Submissions Resolved", 
        "Number of Site Visits", 
        "Active Users",
        "Project Owner",
        "Project Mobile User",
        "Site Owner",
        "Number of Total Submissions", 
        "Number of Pending Submissions", 
        "Number of Approved Submissions", 
        "Number of Flagged Submissions", 
        "Number of Rejected Submissions", 
        "Number of In Progress Submissions", 
        "Total Reviews", 
        "Submissions Flagged", 
        "Submissions Rejected", 
        "Submissions Approved", 
        "Submissions In Progress", 
        "Submissions Resolved"
]

forminfo = [
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
]

def editsiterepo():
    driver.get("https://zite.zite.io/#/projects/416?tab=reports")
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("(//i[@class='material-icons'][normalize-space()='more_vert'])[1]").click()
    driver.find_element_by_xpath("//span[text()='Edit']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//span[text()='Continue']").click()
    driver.implicitly_wait(3)
    
    
    for ps in Po:
        print(ps)
        driver.find_element_by_xpath("//p[text()='{}']".format(ps)).click()
        
    for cases in case:
        driver.find_element_by_xpath("//a[text()='{}']".format(cases)).click()
        print(cases)
        driver.find_element_by_xpath("//span[text()='Save']").click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//span[text()='Save']").click()
        print (driver.current_url)
        path = pathlib.PurePath(driver.current_url)
        id = path.name
        api = "https://zite.zite.io/api/v2/custom-report/report-data/{}".format(id) 
        resp = requests.get("{}".format(api),headers=header)
        if resp.status_code != 200:
            print(*[cases, resp.status_code, resp.json()])
            driver.find_element_by_xpath("//span[text()='Back']").click()
        else:
            print("else")
            driver.send_keys(Keys.CONTROL+'t')
            driver.get("https://zite.zite.io/#/projects/416?tab=reports")
            driver.implicitly_wait(10)
            driver.find_element_by_xpath("(//i[@class='material-icons'][normalize-space()='more_vert'])[1]").click()
            driver.find_element_by_xpath("//span[text()='Edit']").click()
            driver.implicitly_wait(3)
            driver.find_element_by_xpath("//span[text()='Continue']").click()
            driver.implicitly_wait(3)
             
editsiterepo()

def forminfoo():
    driver.get("https://zite.zite.io/#/projects/416?tab=reports")
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("(//i[@class='material-icons'][normalize-space()='more_vert'])[1]").click()
    driver.find_element_by_xpath("//span[text()='Edit']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//span[text()='Continue']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//span[text()='Form Information']").click()
    driver.find_element_by_xpath("//p[text()='Form2.0']").click()
    for questions in forminfo:
        try:
            driver.find_element_by_xpath("//a[text()='{}']".format(questions)).click()
        except:
            driver.find_element_by_xpath("//p[text()='{}']".format(questions)).click()
        driver.find_element_by_xpath("//span[text()='Create']").click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//span[text()='Save']").click()
        print (driver.current_url)
        path = pathlib.PurePath(driver.current_url)
        id = path.name
        api = "https://zite.zite.io/api/v2/custom-report/report-data/{}".format(id) 
        resp = requests.get("{}".format(api),headers=header)
        if resp.status_code != 200:
            print(*[questions, resp.status_code, resp.json()])
            driver.find_element_by_xpath("//span[text()='Back']").click()
        else:
            pass
forminfoo()
