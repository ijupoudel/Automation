from login import loginuser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from login import driver
import time

loginuser()

driver.find_element_by_xpath("//span[text()='Teams']").click()
time.sleep(5)
driver.find_element_by_xpath("//span[text()='Projects']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//span[text()='Sites']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//span[text()='Users']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//span[text()='Forms']").click()
driver.implicitly_wait(5)










driver.close()







