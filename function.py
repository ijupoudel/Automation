
# from login import driver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
import select
import random
import string
s = 5





def get(driver



):
     driver.get('http://zite.zite.io/')


def create_team(driver):
     ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
     driver.find_element_by_xpath("//span[text()='Teams']").click()
     driver.implicitly_wait(5)
     driver.find_element_by_xpath("//span[text()='create new']").click()

     driver.find_element_by_id('id').send_keys(str(ran))
     driver.find_element_by_id('name').send_keys('{}'.format(str(ran)))
     driver.find_element_by_id('address').send_keys('{}'.format(str(ran)))
     driver.find_element_by_xpath("//span[text()='Select']").click()
     driver.implicitly_wait(3)
     driver.find_element_by_xpath("//span[text()='Nepal']").click()
     driver.find_element_by_xpath("//span[text()='Select']").click()
     driver.implicitly_wait(3)
     try:
          driver.find_element_by_xpath("//span[text()='Type A']").click()
     except:
          driver.find_element_by_xpath("//span[text()='Government']").click()
     driver.find_element_by_xpath("//span[text()='Save']").click()
     driver.implicitly_wait(5)


def project_from_teamdashboard(driver):
     ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
     driver.find_element_by_xpath("//span[text()='Create new']").click()
     driver.find_element_by_name('identifier').send_keys((str(ran)))
     driver.find_element_by_name('name').send_keys('{}'.format(str(ran)))
     try:
          driver.find_element_by_name('address').send_keys('{}'.format(str(ran)))
     except:
          pass
     driver.find_element_by_xpath("//span[text()='Select']").click()
     driver.implicitly_wait(3)
     driver.find_element_by_xpath("//span[text()='Nepal']").click()
     try:
          driver.find_element_by_id('lat').send_keys('28.3949')
          driver.find_element_by_id('long').send_keys('84.1240')
     except:
          pass
     driver.find_element_by_xpath("//span[text()='Select']").click()
     driver.implicitly_wait(3)
     driver.find_element_by_xpath("//span[text()='EDUCATION']").click()
     try:
          driver.find_element_by_xpath("//span[text()='Select']").click()
          driver.implicitly_wait(3)
          driver.find_element_by_xpath("//span[text()='Other Education']").click()
     except:
          pass
     driver.find_element_by_id('enable_workflow_yes').click()
     driver.find_element_by_id('cluster_sites_yes').click()
     driver.find_element_by_id('enable_subsites_no').click()
     try:
          driver.find_element_by_name('file').send_keys("/home/queen/Pictures/Screenshots/Screenshot from 2022-06-16 13-47-29.png")
     except:
          pass
     driver.find_element_by_xpath("//span[text()='Save']").click()
# project_from_teamdashboard()
     driver.implicitly_wait(15) 

def site_from_project_dashbboard(driver):
     
     driver.implicitly_wait(5)
     driver.find_element_by_xpath("//i[normalize-space()='add_circle']").click()
     driver.switch_to.window(driver.window_handles[1])
     site_form(driver)

def site_form(driver):
     ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
     driver.find_element_by_name('identifier').send_keys((str(ran)))
     driver.find_element_by_name('name').send_keys('{}'.format(str(ran)))
     driver.find_element_by_xpath("//span[text()='Select']").click()
     driver.implicitly_wait(3)
     try:
          driver.find_element_by_xpath("//span[text()='Sijan']").click
     except:
          pass
     driver.find_element_by_xpath("//span[text()='Select']").click
     driver.implicitly_wait(3)
     try:
          driver.find_element_by_xpath("//span[text()='QA']").click
     except:
          pass
     driver.find_element_by_name('address').send_keys('{}'.format(str(ran)))
     driver.find_element_by_name('description').send_keys('This is description of mouse{}'.format(str(ran)))
     driver.find_element_by_id('geojsontext').send_keys('{"type":"FeatureCollection","features":[{"type":"Feature","geometry":{"type":"Point","coordinates":[84.69645843750001,27.825931411527606]},"properties":null}]}')
     driver.find_element_by_xpath('//button[contains(text(), "Apply")]').click()
     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
     driver.find_element_by_name('file').send_keys("/home/queen/Pictures/Screenshots/Screenshot from 2022-06-16 13-47-29.png")
     driver.find_element_by_xpath("//span[text()='Save']").click()
     driver.implicitly_wait(5)

def create_project(driver):
     ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
     driver.find_element_by_xpath("//span[text()='Projects']").click()
     driver.implicitly_wait(5)
     driver.find_element_by_xpath("//span[text()='create new']").click()
     
     driver.find_element_by_name('identifier').send_keys(str(ran))
     driver.find_element_by_name('name').send_keys('{}'.format(str(ran)))
     driver.find_element_by_name('address').send_keys('{}'.format(str(ran)))
     driver.find_element_by_xpath("//span[text()='Select']").click()
     driver.implicitly_wait(3)
     driver.find_element_by_xpath("//span[text()='Nepal']").click()
     driver.find_element_by_id('lat').send_keys('28.3949')
     driver.find_element_by_id('long').send_keys('84.1240')
     driver.find_element_by_xpath("//span[text()='Select']").click()
     driver.implicitly_wait(3)
     driver.find_element_by_xpath("//span[text()='mouse']").click()
     driver.find_element_by_xpath("//span[text()='Select']").click()
     driver.implicitly_wait(3)
     driver.find_element_by_xpath("//span[text()='EDUCATION']").click()
     driver.find_element_by_xpath("//span[text()='Select']").click()
     driver.implicitly_wait(3)
     driver.find_element_by_xpath("//span[text()='Other Education']").click()
     driver.find_element_by_id('enable_workflow_yes').click()
     driver.find_element_by_id('cluster_sites_yes').click()
     driver.find_element_by_id('enable_subsites_no').click()
     try:
          driver.find_element_by_name('file').send_keys("/home/queen/Pictures/Screenshots/Screenshot from 2022-06-16 13-47-29.png")
     except:
          pass
     driver.find_element_by_xpath("//span[text()='Save']").click()
     driver.implicitly_wait(5)

def create_site(driver):
     driver.find_element_by_xpath("//span[text()='Sites']").click()
     driver.implicitly_wait(3)
     driver.find_element_by_xpath("//span[text()='create new']").click()
     driver.implicitly_wait(10)
     driver.find_element_by_xpath("(//tr)[40]").click()
     site_form()

