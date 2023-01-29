from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from login import driver
import random
import string
s = 5 
# driver.get('https://zite.zite.io/user/signup')
ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = s))  
print(ran)
def signup():
    username = driver.find_element_by_id("id_username")
    username.send_keys(str(ran))
    email = driver.find_element_by_id("id_email")
    email.send_keys('cfp.zite+{}@gmail.com'.format(str(ran)))
    password = driver.find_element_by_id("id_password")
    password.send_keys('Apple.123')
    password1 = driver.find_element_by_id("id_password1")
    password1.send_keys('Apple.123')
    privacy = driver.find_element_by_id("privacy")
    privacy.click()
    submit = driver.find_element_by_id("btn-signup")
    submit.click()
signup()
