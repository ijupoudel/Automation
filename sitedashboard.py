from login import driver
import time
import random
import string
from selenium.webdriver.common.keys import Keys
import calendar
from datetime import date

def selectsitefromlist():
    driver.find_element_by_xpath("//span[text()='Sites']").click()
    driver.implicitly_wait(20)
    a = driver.find_elements_by_xpath("//tr")
    b = (len(a))
    print(b)
    anysite = random.randint(1,b)
    driver.find_element_by_xpath("//tr[{}]".format(anysite)).click()
    driver.implicitly_wait(5)

def selectformtomakesubmission():
    driver.find_element_by_xpath("//i[@class='material-icons'][normalize-space()='add_circle']").click()
    driver.implicitly_wait(3)
    a = driver.find_elements_by_xpath("//i[@class='material-icons'][normalize-space()='add']")
    b = len(a)
    print(b)
    selectform = random.randint(1, b)
    driver.find_element_by_xpath("//tr[{}]//i[@class='material-icons'][normalize-space()='add']".format(selectform)).click()
    driver.switch_to.window(driver.window_handles[1])






