import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome('//home/queen/Desktop/naxa/zite-automation/chromedriver') 
user = [
    "sijuteamowner",
    "sijuprojectowner",
    "sijusiteowner",
    "sijusitemobile",
    "projectmobile",
    "sijuteammobile",
    "sijuteammanager",
    "sijuprojectmanager",
    "sijusitemanager",
    "sijuteamreviewer",
    "sijuprojectreviewer",
    "sijusitereviewer",
    "sijuteameditior",
    "sijuprojecteditior",
    "sijusiteeditior",
    "sijuprojectfocal2",
    "sijusitefocal1",  
]
driver.get('https://zite.zite.io/')
driver.execute_script('''window.open("","_blank");''')

for users in user:
    
    username = driver.find_element_by_id("id_email_or_username")
    print(users)
    username.send_keys(users)
    password = driver.find_element_by_id("id_password")
    password.send_keys('wv1nep@l')
    driver.find_element_by_id("login").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//a[@class='user-avatar is-horiz is-center is-align-center']").click()
    
    driver.find_element_by_xpath("//span[text()='Edit Profile']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//span[text()='Email']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//div[@class='flat-radio ']//input[@id='Monthly']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//span[text()='Save']").click()
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://zite.zite.io/api/v2/email-test/?frequency=Monthly")
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element_by_xpath("//a[@class='user-avatar is-horiz is-center is-align-center']").click()
    time.sleep(10)
    driver.find_element_by_xpath("//span[text()='Log Out']").click()
    driver.implicitly_wait(5)
