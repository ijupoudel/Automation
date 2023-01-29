from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('//home/queen/Desktop/naxa/zite-automation/chromedriver')
search = driver.find_element_by_id("search")
search.send_keys(Keys.CONTROL+'t') 
header = {
        'Authorization':'token 1f78420bfd4d2fdc9c52851098e3419787a5dbe7'
    }
Po = [
    "Number of Submissions",
    "Submissions Reviewed", 
    "Active Users by Role",
    "Individual Form Metrics",
    "Form2.0"

]
orminfo = [
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
def pps():
    
        for ps in Po:
            print(ps)
        for forms in orminfo:
            api = "https://zite.zite.io/api/v2/custom-report/report-data/1912".format(id) 
            resp = requests.get("{}".format(api),headers=header)
            if resp.status_code != 200:
                print(*[api, resp.status_code, resp.json()])
                driver.find_element_by_xpath("//span[text()='Back']").click()
            else:
                driver.get("https://zite.zite.io/#/projects/416?tab=reports")
pps()