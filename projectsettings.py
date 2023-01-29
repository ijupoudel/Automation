from selenium import webdriver
# from login import driver
import time
import random
import string
from selenium.webdriver.common.keys import Keys
import calendar
from datetime import date
s = 5

def selectproject(driver):
    driver.find_element_by_xpath("//span[text()='Projects']").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//div[@class='org'][1]").click()
    driver.implicitly_wait(5)
# Select project settings from project dashboard
def project_settings(driver):
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//i[text()='settings']").click()


# Select forms and data
def formsanddata(driver):
    driver.find_element_by_xpath("//span[text()='Forms and Data']").click()
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[1])



# Assign general form
def assigngeneralform(driver):
    driver.find_element_by_xpath("//li[@data-tab='GENERAL_FORM']").click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath("//span[text()='assign new']").click() 
    driver.implicitly_wait(5) 
    driver.find_element_by_xpath("//span[text()='choose form']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("(//div[contains(@class,'general-form-content')])[3]").click()

    # Select random status
    try:
        statuslist = ['Pending', 'Flagged', 'Rejected', 'In Progress', 'Approved']
        status = random.choice(tuple(statuslist))
        driver.find_element_by_id('{}'.format(status)).click()
    except:
        pass
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//p[text()='Advanced Settings']").click() 
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//span[text()='assign']").click()
    driver.implicitly_wait(3)



# Assign Schedule Form
def assignscheduleform(driver):
    driver.find_element_by_xpath("//li[@data-tab='SCHEDULE_FORM']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//span[text()='assign new']").click() 
    driver.implicitly_wait(5) 
    driver.find_element_by_xpath("//span[text()='choose form']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("(//div[contains(@class,'general-form-content')])[5]").click()
    
    # Select random status
    try:
        statuslist = ['Pending', 'Flagged', 'Rejected', 'In Progress', 'Approved']
        status = random.choice(tuple(statuslist))
        driver.find_element_by_id('{}'.format(status)).click()
    except:
        pass
    driver.find_element_by_xpath("//p[text()='Advanced Settings']").click()

    # Select random schedule
    schedule = ['weekly', 'daily', 'monthly']
    scheduletype = random.choice(tuple(schedule))
    driver.find_element_by_id(scheduletype).click()

    # If weeekly
    if (scheduletype == 'weekly'):
        driver.find_element_by_xpath("//span[text()='Select']").click()
        numberweek = range(1, 52)
        week = random.choice(numberweek)
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//li[@role='menuitem']//span[text()='{}']".format(week)).click()
        driver.find_element_by_xpath("//span[text()='Select']").click()
        every = list(calendar.day_name)
        day = random.choice(every)
        print (day)
        driver.find_element_by_xpath("//span[text()='{}']".format(day)).click()

    # If Daily
    elif (scheduletype == 'daily'):
        driver.find_element_by_xpath("//span[text()='Select']").click()
        every = list(calendar.day_name)
        day = random.choice(every)
        print (day)
        driver.find_element_by_xpath("//div[@class='custom-checkbox']//label[text()='{}']".format(day)).click()
        # driver.find_element_by_xpath("//div[@class='custom-select']").click()
        
    #  If Monthly
    else :
        driver.find_element_by_xpath("//span[text()='Select']").click()
        numbermonth = range(1, 12)
        month = random.choice(numbermonth)
        driver.find_element_by_xpath("//li[@role='menuitem']//span[normalize-space()='{}']".format(month)).click()
        driver.find_element_by_xpath("//span[text()='last of month']").click()
        numberdate = range(1, 31)
        dateday = random.choice(numberdate)
        if dateday == 31:
            driver.find_element_by_xpath("//li[@role='menuitem']//span[text()='last of month]").click() 
        else:
            driver.find_element_by_xpath("//li[@role='menuitem']//span[text()='{}']".format(dateday)).click()

    #  Select Random Start schedule
    start = ['Immediately', 'on_first_submission', 'selected_date']
    starttype = random.choice(tuple(start))
    driver.implicitly_wait(3)
    driver.find_element_by_id(starttype).click()
    if (starttype == 'selected_date'):
        datec = date.today()
        today = datec.strftime('%d/%m/%Y')
        driver.find_element_by_xpath("//span[text()='{}']".format(today)).click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//span[text()='{}']".format(datec.strftime('%B %Y'))).click()
        driver.find_element_by_xpath("//span[text()='{}']".format(datec.strftime('%Y'))).click()
        driver.implicitly_wait(5)
        yeard = random.choice(range(1,10))
        driver.find_element_by_xpath("//button[@class='react-calendar__tile react-calendar__decade-view__years__year'][{}]".format(yeard)).click()
        numbermonth = range(1, 12)
        month = random.choice(numbermonth)
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//button[@class='react-calendar__tile react-calendar__year-view__months__month'][{}]".format(month)).click()
        try:
            driver.find_element_by_xpath("//button[@class='react-calendar__tile react-calendar__month-view__days__day'][{}]".format(random.choice(range(1, 20)))).click()
        except:
            driver.find_element_by_xpath("//button[@class='react-calendar__tile react-calendar__month-view__days__day react-calendar__month-view__days__day--weekend'][{}]".format(random.choice(range(1, 10)))).click()
        driver.implicitly_wait(5)
        
    else:
        pass

    # Select Random End Schedule
    end = ['Never', 'Afte_Submissions', 'EndDate']
    endtype = random.choice(tuple(end))
    driver.find_element_by_id(endtype).click()
    if (endtype == 'Afte_Submissions'):
        driver.find_element_by_name('end_after_submission').send_keys('5')
    elif(endtype == 'EndDate'):
        datec = date.today()
        today = datec.strftime('%d/%m/%Y')
        driver.find_element_by_xpath("//span[text()='{}']".format(today)).click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//span[text()='{}']".format(datec.strftime('%B %Y'))).click()
        driver.find_element_by_xpath("//span[text()='{}']".format(datec.strftime('%Y'))).click()
        driver.implicitly_wait(5)
        yeard = random.choice(range(1,10))
        driver.find_element_by_xpath("//button[@class='react-calendar__tile react-calendar__decade-view__years__year'][{}]".format(yeard)).click()
        numbermonth = range(1, 12)
        month = random.choice(numbermonth)
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//button[@class='react-calendar__tile react-calendar__year-view__months__month'][{}]".format(month)).click()
        try:
            driver.find_element_by_xpath("//button[@class='react-calendar__tile react-calendar__month-view__days__day'][{}]".format(random.choice(range(1, 20)))).click()
        except:
            driver.find_element_by_xpath("//button[@class='react-calendar__tile react-calendar__month-view__days__day react-calendar__month-view__days__day--weekend'][{}]".format(random.choice(range(1, 10)))).click()
    else:
        pass

    notify = ['yes', 'no']
    driver.find_element_by_id(random.choice(tuple(notify))).click()
    driver.find_element_by_xpath("//span[text()='assign']").click()
    driver.implicitly_wait(3)


# Create Stage
def stageform(driver):
    driver.find_element_by_xpath("//span[text()='staged Forms']").click()
# add stage
def addstage(driver):
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = s))
    driver.find_element_by_xpath("//span[text()='Add stage']").click()
    driver.find_element_by_id('name').send_keys(ran)
    driver.find_element_by_name('description').send_keys('This is description')
    driver.find_element_by_name('weight').send_keys(random.randint(0,10))
    driver.find_element_by_xpath("//div[@class='zite-lg-6'][{}]".format(random.randint(1,4))).click()
    driver.find_element_by_xpath("//span[text()='add']").click()

def assignstageform(driver):
    driver.find_element_by_xpath("//span[text()='assign new']").click() 
    driver.implicitly_wait(5) 
    driver.find_element_by_xpath("//span[text()='choose form']").click()
    driver.implicitly_wait(3)
    a = driver.find_elements_by_xpath("(//div[contains(@class,'general-form-content')])")
    b = len(a)
    c = random.randint(1, b)
    driver.find_element_by_xpath("(//div[contains(@class,'general-form-content')])[{}]".format(c)).click()
     # Select random status
    try:
        statuslist = ['Pending', 'Flagged', 'Rejected', 'In Progress', 'Approved']
        status = random.choice(tuple(statuslist))
        driver.find_element_by_id('{}'.format(status)).click()
    except:
        pass
    driver.find_element_by_xpath("//p[text()='Advanced Settings']").click() 
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//span[text()='assign']").click()
    driver.implicitly_wait(3)

def addformtostage(driver):

    a =  driver.find_elements_by_xpath("//ul[@class='list is-border is-checkbox']")
    c= len(a)
    b = random.randint(1, c)
    print(c)
    try: 
        driver.find_element_by_xpath("//ul[@class='list is-border is-checkbox'][1]//ul[@class='inline-row is-checkbox'][{}]//div[@class='custom-checkbox'][{}]//input[@type='checkbox'][{}]".format(b,1,1)).click()
    except:
        driver.find_element_by_xpath("//ul[@class='list is-border is-checkbox'][2]//ul[@class='inline-row is-checkbox'][{}]//div[@class='custom-checkbox'][{}]//input[@type='checkbox'][{}]".format(b,1,1)).click()
    driver.find_element_by_xpath("//a[normalize-space()='Move']").click()
    

def addprojectform(driver):
    driver.find_element_by_xpath("//li[@data-tab='PROJECT_GENERAL_FORM']").click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath("//span[text()='assign new']").click() 
    driver.implicitly_wait(5) 
    driver.find_element_by_xpath("//span[text()='choose form']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("(//div[contains(@class,'general-form-content')])[3]").click()

    # Select random status
    statuslist = ['Pending', 'Flagged', 'Rejected', 'In Progress', 'Approved']
    status = random.choice(tuple(statuslist))
    driver.find_element_by_id('{}'.format(status)).click()
    driver.find_element_by_xpath("//p[text()='Advanced Settings']").click() 
    driver.find_element_by_xpath("//span[text()='assign']").click()








#  Deploy Form
def deploy(driver):
    driver.find_element_by_xpath("(//i[@class='material-icons'][normalize-space()='more_vert'])[1]").click()
    driver.find_element_by_xpath("//span[text()='Deploy']").click()
    driver.find_element_by_xpath('//button[text()="Confirm"]').click()


# Edit Form For General form
def edit(driver):
    driver.find_element_by_xpath("(//i[@class='material-icons'][normalize-space()='more_vert'])[2]").click()
    driver.find_element_by_xpath("//span[text()='Edit']").click()
    statuslist = ['Pending', 'Flagged', 'Rejected', 'In Progress', 'Approved']
    status = random.choice(tuple(statuslist))
    driver.find_element_by_id('{}'.format(status)).click()
    driver.find_element_by_xpath("//h5[text()='Advanced Settings']").click() 
    driver.find_element_by_xpath("//span[text()='assign']").click()


# Add form Summary
def summary(driver):
    driver.implicitly_wait(2)
    driver.find_element_by_xpath("(//i[@class='material-icons'][normalize-space()='more_vert'])[2]").click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath("(//i[@class='material-icons'][normalize-space()='summarize'])[2]").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("(//div[contains(@class,'add-remove')])[2]").click()
    driver.find_element_by_xpath("//button[text()='Save']").click()


# Select workflow
def workflow(driver):
    driver.implicitly_wait(2) 
    driver.find_element_by_xpath("(//i[@class='material-icons'][normalize-space()='more_vert'])[1]").click()
    driver.find_element_by_xpath("(//i[@class='material-icons'][normalize-space()='alt_route'])[1]").click()
    driver.switch_to.window(driver.window_handles[2])
    driver.implicitly_wait(2)
    

# group workflow
def group(driver):
    driver.find_element_by_xpath("//span[text()='create new']").click()
    driver.implicitly_wait(3)
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = s))  
    driver.find_element_by_name('name').send_keys(str(ran))
    driver.find_element_by_xpath("//input[@id='group']").click()
    driver.find_element_by_xpath("//li[@data-index='1']").click()
    driver.find_element_by_xpath("//a[text()='Answer match']").click()
    driver.find_element_by_xpath("//span[text()='create']").click()


# Refer workflow
def refer(driver):
    driver.find_element_by_xpath("//span[text()='create new']").click()
    driver.implicitly_wait(3)
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = s))  
    driver.find_element_by_name('name').send_keys(str(ran))
    driver.find_element_by_xpath("//input[@id='refer']").click()
    driver.find_element_by_xpath("//li[@data-index='0']").click()
    try: 
        driver.find_element_by_xpath("//ul[@class='list is-plus pd-0']//li[@data-index='1']").click()
    except:
        driver.find_element_by_xpath("//input[@class='font-control']").send_keys('apple')
        driver.find_element_by_xpath("//i[text()='add_circle_outline']").click()
    driver.find_element_by_id('any').click()

    # Refer any user
    referusers = ['users', 'roles']
    referee = (random.choice(tuple(referusers)))
    driver.find_element_by_xpath("//input[@id='{}']".format(referee)).click()
    print(referee)
    driver.implicitly_wait(3)
    if (referee == 'users'): 
        driver.find_element_by_xpath("//span[text()='Select']").click()
        driver.find_element_by_xpath("//p[@tabindex='0']").click()
        print("success")
        driver.implicitly_wait(2)
    else:
        driver.find_element_by_id('33').click()
    driver.find_element_by_xpath("//span[text()='create']").click()
    driver.implicitly_wait(5)


# Escalate Workflow
def escalate(driver):
    driver.find_element_by_xpath("//span[text()='create new']").click()
    driver.implicitly_wait(3)
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = s))  
    driver.find_element_by_name('name').send_keys(str(ran))
    driver.find_element_by_xpath("//input[@id='escalate']").click()
    driver.implicitly_wait(5)

    # Select random escalate type
    escalatetype = ['time', 'criteria']
    driver.find_element_by_id(random.choice(tuple(escalatetype))).click()
    if (escalatetype == 'criteria'):
        driver.find_element_by_id('criteria').click()
        driver.find_element_by_xpath("//li[@data-index='0']").click()
        try: 
            driver.find_element_by_xpath("//ul[@class='list is-plus pd-0']//li[@data-index='1']").click()
        except:
            driver.find_element_by_xpath("//input[@class='font-control']").send_keys('apple')
            driver.find_element_by_xpath("//i[text()='add_circle_outline']").click()
            driver.find_element_by_id('any').click()
    else:
        pass
    driver.find_element_by_xpath("//input[@type='number']").send_keys('2')
    driver.find_element_by_xpath("//span[text()='Select']").click()
    driver.find_element_by_xpath("//ul[@class='select-list left-dropdown']//li[@role='menuitem'][2]").click()

    # Select random roles or user to escalate
    referusers = ['users', 'roles']
    referee = (random.choice(tuple(referusers)))
    driver.find_element_by_xpath("//input[@id='{}']".format(referee)).click()
    print(referee)
    driver.implicitly_wait(3)
    if (referee == 'users'): 
        driver.find_element_by_xpath("//input[@id='users']").click()
        driver.find_element_by_xpath("//span[text()='Select']").click()
        driver.find_element_by_xpath("//p[@tabindex='0']").click()
        print("success")
        driver.implicitly_wait(2)
    else:
        driver.find_element_by_id('33').click()
    driver.find_element_by_xpath("//span[text()='create']").click()
    driver.implicitly_wait(5)
    

# Follow type Workflow
def follow(driver):
    driver.find_element_by_xpath("//span[text()='create new']").click()
    driver.implicitly_wait(3)
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = s))  
    driver.find_element_by_name('name').send_keys(str(ran))
    driver.find_element_by_xpath("//input[@id='follow-up']").click()
    driver.find_element_by_xpath("//li[@data-index='0']").click()
    try: 
        driver.find_element_by_xpath("//ul[@class='list is-plus pd-0']//li[@data-index='1']").click()
    except:
        driver.find_element_by_xpath("//input[@class='font-control']").send_keys('apple')
        driver.find_element_by_xpath("//i[text()='add_circle_outline']").click()
    driver.find_element_by_id('any').click()
    driver.find_element_by_xpath("//span[text()='Select']").click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//ul[@class='select-list left-dropdown']//li[@role='menuitem'][1]").click()
    driver.find_element_by_id('individual-submission').click()
    driver.implicitly_wait(5)


#  Immediate Follow
def immediate_follow(driver):
    driver.find_element_by_id('immediate').click()
    driver.find_element_by_xpath("//span[text()='create']").click()
    driver.implicitly_wait(5)


#  Follow when status is changed
def after_status(driver):
    driver.find_element_by_id('form-status').click()
    driver.find_element_by_xpath("//span[text()='Select']").click()

    # Select Random status for followup
    status = ['Pending', 'Flagged', 'In Progress', 'Rejected', 'Approved']

    driver.find_element_by_xpath("//span[text()='{}']".format(random.choice(tuple(status)))).click()
    
    driver.find_element_by_xpath("//span[text()='create']").click()
    driver.implicitly_wait(5)


# Change status workflow 
def change_status(driver):
    driver.find_element_by_xpath("//span[text()='create new']").click()
    driver.implicitly_wait(3)
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = s))  
    driver.find_element_by_name('name').send_keys(str(ran))
    driver.find_element_by_xpath("//input[@id='change-status']").click()
    driver.find_element_by_xpath("//li[@data-index='1']").click()
    driver.find_element_by_xpath("//ul[@class='list is-plus pd-0']//li[@data-index='1']").click()
    driver.find_element_by_id('all').click()
    driver.find_element_by_xpath("//span[text()='Select']").click()
    driver.implicitly_wait(3)
    n = random.choice(tuple(range(1,5)))
    driver.find_element_by_xpath("//ul[@class='select-list left-dropdown']//li[@role='menuitem'][{}]".format(n)).click()
    driver.find_element_by_xpath("//span[text()='create']").click()
    driver.implicitly_wait(5)


# hide workflow
def hide(driver):
    driver.find_element_by_xpath("//span[text()='create new']").click()
    driver.implicitly_wait(3)
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = s))  
    driver.find_element_by_name('name').send_keys(str(ran))
    driver.find_element_by_xpath("//input[@value='HIDE']").click()
    driver.find_element_by_xpath("//li[@data-index='0']").click()
    try: 
        driver.find_element_by_xpath("//ul[@class='list is-plus pd-0']//li[@data-index='1']").click()
    except:
        driver.find_element_by_xpath("//input[@class='font-control']").send_keys('apple')
        driver.find_element_by_xpath("//i[text()='add_circle_outline']").click()
    driver.find_element_by_id('any').click()
    referusers = ['users', 'roles']
    referee = (random.choice(tuple(referusers)))
    driver.find_element_by_xpath("//input[@id='{}']".format(referee)).click()
    print(referee)
    driver.implicitly_wait(3)
    if (referee == 'users'): 
        driver.find_element_by_xpath("//input[@id='users']").click()
        driver.find_element_by_xpath("//span[text()='Select']").click()
        driver.find_element_by_xpath("//p[@tabindex='0']").click()
        print("success")
        driver.implicitly_wait(2)
    else:
        driver.find_element_by_id('33').click()
    driver.find_element_by_xpath("//span[text()='create']").click()
    driver.implicitly_wait(5)


# Tag workflow
def tag(driver):
    driver.find_element_by_xpath("//span[text()='create new']").click()
    driver.implicitly_wait(3)
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = s))  
    driver.find_element_by_name('name').send_keys(str(ran))
    driver.find_element_by_xpath("//input[@value='TAG']").click()
    driver.find_element_by_xpath("//li[@data-index='1']").click()
    driver.find_element_by_xpath("//ul[@class='list is-plus pd-0']//li[@data-index='1']").click()
    driver.find_element_by_id('all').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//span[text()='Add More Tag To Project']").click()
    driver.find_element_by_xpath("//input[@placeholder='Add Tag']").send_keys(str(ran))
    driver.find_element_by_xpath("//input[@placeholder='Add Tag']").send_keys(Keys.ENTER)
    driver.implicitly_wait(3)
    driver. find_element_by_xpath("//div[@class='is-parent'][1]").click()
    driver.implicitly_wait(3)
    try:
        driver. find_element_by_xpath("//div[@class='is-parent'][5]").click()
        driver.implicitly_wait(3)
    except:
        pass
    driver. find_element_by_xpath("//input[@id='Age']").click()
    driver.find_element_by_xpath("//span[text()='create']").click()
    driver.implicitly_wait(5)


def user(driver):
    driver.find_element_by_xpath("//a[@target='_blank']//span[contains(text(),'Users')]").click()
    driver.switch_to.window(driver.window_handles[2])
    driver.implicitly_wait(5)

# Add new user while assigning  User
def create_user(driver):

    driver.implicitly_wait(3)
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = s))  
    driver.find_element_by_xpath("//i[text()='add_circle']"). click()
    driver.find_element_by_name('first_name').send_keys(str(ran))
    driver.find_element_by_name('last_name').send_keys(str(ran))
    driver.find_element_by_name('username').send_keys(str(ran))
    driver.find_element_by_name('Female').click()
    driver.find_element_by_name('password').send_keys('wv1nep@l')
    driver.find_element_by_name('passwordcheck').send_keys('wv1nep@l')
    driver.find_element_by_xpath("//a[normalize-space()='Mobile User']").click()
    driver.find_element_by_xpath("//span[text()='Save']").click()
    driver.refresh()
    driver.implicitly_wait(3)
# create_user()

def number(driver):

    i = 5
    for i in range (i+1):
        create_user(driver)


def addtags(driver):
    driver.switch_to.window(driver.window_handles[2])
    driver.find_element_by_xpath("//span[text()='Tags Management']").click()
    driver.find_element_by_xpath("//input[@placeholder='Add Tag']").send_keys('tag{}'.format(random.randint(1, 10)))
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Add Tag']").send_keys(Keys.ENTER)


def addreason(driver):
    driver.switch_to.window(driver.window_handles[2])
    driver.find_element_by_xpath("//span[text()='Submission Reasons']").click()
    driver.find_element_by_xpath("//input[@placeholder='Add Reason']").send_keys('reason{}'.format(random.randint(1, 10)))
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//input[@placeholder='Add Reason']").send_keys(Keys.ENTER)

# driver.switch_to.window(driver.window_handles[0])
# driver.find_element_by_xpath("//i[text()='post_add']").click()

def projectforworkflow(driver):
    driver.get ("https://zite.zite.io/#/projects/370")
