import unittest
from selenium import webdriver
import softest
import pathlib

class ExampleTest(softest.TestCase):
    # test function to test equality of two value
    def test_negative(self):
        driver = webdriver.Chrome('//home/queen/Desktop/naxa/zite-automation/chromedriver') 
        driver.get("https://zite.zite.io")
        print(driver.title)
        self.soft_assert(self.assertEqual, "Zite is a pl--atform for remote supervision and monitoring", driver.title, 'Not same')

        self.login()

    def login(self):
        driver = webdriver.Chrome('//home/queen/Desktop/naxa/zite-automation/chromedriver') 
        driver.get('https://zite.zite.io/')
        username = driver.find_element_by_id("id_email_or_username")
        username.send_keys('super_admin')
        password = driver.find_element_by_id("id_password")
        password.send_keys('c_)a}H#w6oXD')
        driver.find_element_by_id("login").click()
        path = pathlib.PurePath(driver.current_url)
        print(path.name)
        self.assertEqual("dashboard", path.name, 'Not same')
        
        self.assert_all()

if __name__ == '__main__':
    softest.main()