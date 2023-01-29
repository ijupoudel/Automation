from psutil import users
from login import loginusercfp, loginuserzitemagaer, loginuserziteprod, loginuserzitestaging
from selenium import webdriver
from enketoformforvushan import form
from selenium.webdriver.support.ui import WebDriverWait
from function import create_team, project_from_teamdashboard, site_from_project_dashbboard
from projectsettings import addprojectform, addreason, after_status, change_status, escalate, follow, group, hide, immediate_follow, number, project_settings, projectforworkflow, refer, tag, user, addtags, formsanddata, assigngeneralform, deploy, selectproject, stageform, assignscheduleform, assignstageform, addstage, addformtostage, workflow

print("\n Select One from the following URL")
url_dict = {
	1: 'zite.zite.io',
	2: 'app.zite.io',
	3: 'cfp.zite.io',
	4: 'www.commonfeedbackplatform.org',
    5: 'app.zitemanager.org'
}
print(f"1). {url_dict[1]}")
print(f"2). {url_dict[2]}")
print(f"3). {url_dict[3]}")
print(f"4). {url_dict[4]}")
print(f"5). {url_dict[5]}")

inp = int(input("Please Enter a number: "))

print("\n Select one from following features ")
features = {
    1: 'Create Team,project and site',
    2: 'Assign and deploy general from',
    3: 'Assign and deploy Schedule Form',
    4: 'Assign and deploy staged form',
    5: 'Fill a form on staging only',
    6: 'Assign and deploy project general form',
    7: 'Add workflows to existing form(staging)',
    
}
print(f"1). {features[1]}")
print(f"2). {features[2]}")
print(f"3). {features[3]}")
print(f"4). {features[4]}")
print(f"5). {features[5]}")
print(f"6). {features[6]}")
print(f"7). {features[7]}")

feature = int(input("Please Enter a number: "))

print("\n Select one from following additional features ")
additionals = {
    1: 'create users',
    2: 'Add tags',
    3: 'Add Reasons',
    
}

print(f"1). {additionals[1]}")
print(f"2). {additionals[2]}")
print(f"3). {additionals[3]}")


additional = int(input("Please Enter a number: "))

if feature == 5:
    form()

elif feature == 7:
    driver = webdriver.Chrome('//home/queen/Desktop/naxa/zite-automation/chromedriver') 
    driver.maximize_window()
    loginuserzitestaging(driver)
    projectforworkflow(driver)
    project_settings(driver)
    formsanddata(driver)
    workflow(driver)
    refer(driver)
    escalate(driver)
    follow(driver)
    immediate_follow(driver)
    follow(driver)
    after_status(driver)
    change_status(driver)
    hide(driver)
    tag(driver)
    group(driver)

else:
    driver = webdriver.Chrome('//home/queen/Desktop/naxa/zite-automation/chromedriver') 
    driver.maximize_window()


    if inp == 1:
        loginuserzitestaging(driver)

    elif inp == 2:
        loginuserziteprod(driver)

    elif inp in [3, 4]:
        loginusercfp(driver)

    elif inp == 5:
        loginuserzitemagaer(driver)

    else:
        print('INVALID INPUT') 

    if feature == 1:
        create_team(driver)
        project_from_teamdashboard(driver)
        site_from_project_dashbboard(driver)

    elif feature == 2:
        selectproject(driver)
        project_settings(driver)
        formsanddata(driver)
        assigngeneralform(driver)
        deploy(driver)

    elif feature == 3:
        selectproject(driver)
        project_settings(driver)
        formsanddata(driver)
        assignscheduleform(driver)
        deploy(driver)

    elif feature == 4:
        selectproject(driver)
        project_settings(driver)
        formsanddata(driver)
        stageform(driver)
        addstage(driver)
        assignstageform(driver)
        deploy(driver)

    elif feature == 6:
        selectproject(driver)
        project_settings(driver)
        formsanddata(driver)
        addprojectform(driver)
        deploy(driver)

    else:
        print('INVALID INPUT')

    if additional == 1:
        driver.switch_to.window(driver.window_handles[0])
        project_settings(driver)
        user(driver)
        number(driver)
    
    elif additional == 2:
        driver.switch_to.window(driver.window_handles[0])
        project_settings(driver)
        formsanddata(driver)
        addtags(driver)

    elif additional == 3:
        driver.switch_to.window(driver.window_handles[0])
        project_settings(driver)
        formsanddata(driver)
        addreason(driver)

    else:
        pass