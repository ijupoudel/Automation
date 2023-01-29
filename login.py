import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from list import usernames
from list import passe


# driver = webdriver.Chrome('//home/queen/Desktop/naxa/zite-automation/chromedriver') 
# print (driver.title)
# driver.maximize_window()
# driver.get('https://zite.zite.io/')
# url = input("Enter the URL of site you want to visit: ")
# driver.get('http://{}/'.format(url))
# try:
#  driver.find_element_by_xpath("//span[text()='log in']").click()
# except:
#     pass

# username = input("Enter your username or email : ")
# for users in usernames:
#     print(users)
#     try:
#         driver.find_element_by_id(users).send_keys(format(username))
#     except:
#         pass
# try:
#  driver.find_element_by_xpath("//span[text()='Next']").click()
# except:
#     pass
# password = input("Enter your password: ")
# for passes in passe:
#   try:
#    driver.find_element_by_id(passes).send_keys(format(password))
#   except :
#     pass
# try:
#  driver.find_element_by_xpath("//span[text()='Next']").click()
# except:
#     pass


def loginuserzitestaging(driver):
    driver.get('https://zite.zite.io/')
    
    username = driver.find_element_by_id("id_email_or_username")
    username.send_keys('super_admin')
    password = driver.find_element_by_id("id_password")
    password.send_keys('c_)a}H#w6oXD')
    driver.find_element_by_id("login").click()


def loginuserziteprod(driver):
    driver.get('https://app.zite.io/')
    username = driver.find_element_by_id("id_email_or_username")
    username.send_keys('super_admin')
    password = driver.find_element_by_id("id_password")
    password.send_keys('TX/BKiwzr6)8')
    driver.find_element_by_id("login").click()

def loginusercfp(driver):
    driver.get('https://www.commonfeedbackplatform.org/')
    username = driver.find_element_by_id("id_email_or_username")
    username.send_keys('cfp_admin')
    password = driver.find_element_by_id("id_password")
    password.send_keys('ZjrabE3ab4hrIvx3u2EZ')
    driver.find_element_by_id("login").click()

def loginuserzitemagaer(driver):
    driver.get('https://app.zitemanager.org/')
    username = driver.find_element_by_id("id_email_or_username")
    username.send_keys('admin_zitemanager')
    password = driver.find_element_by_id("id_password")
    password.send_keys('kyrv6CDCYJgHnvfF')
    driver.find_element_by_id("login").click()

