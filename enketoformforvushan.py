from itertools import dropwhile
from selenium import webdriver
import time
import random
import string
from selenium.webdriver.common.keys import Keys
from datetime import date, datetime
from login import loginuserzitestaging

def selectform(driver):
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//i[@class='material-icons'][normalize-space()='add_circle']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//tr[2]//i[@class='material-icons'][normalize-space()='add']").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(10)


def fillform(driver):
    name = ['Siju', 'Rohit', 'ROHIT', 'SIJAN', 'SiJaN']
    driver.find_element_by_xpath("//input[@type='text']").send_keys(random.choice(tuple(name)))
    driver.find_element_by_xpath("//input[@type='number']").send_keys(random.randint(1,80))
    a = ['1female', '2male']
    driver.find_element_by_xpath("//input[@value='{}']".format(random.choice(tuple(a)))).click()
    driver.find_element_by_xpath("//input[@data-type-xml='decimal']").send_keys(random.randint(1,80))
    driver.find_element_by_xpath("//input[@placeholder='yyyy-mm-dd']").send_keys('2022-07-12')
    b = ['yes', 'no']
    driver.find_element_by_xpath("//input[@value='{}']".format(random.choice(tuple(b)))).click()
    driver.find_element_by_id("submit-form").click()
    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(10)
    driver.refresh()
    driver.implicitly_wait(10)


def form():
    driver = webdriver.Chrome('//home/queen/Desktop/naxa/zite-automation/chromedriver') 
    driver.maximize_window()
    loginuserzitestaging(driver)
    driver.get ("https://zite.zite.io/#/sites/32463")
    selectform(driver)
    fillform(driver)
