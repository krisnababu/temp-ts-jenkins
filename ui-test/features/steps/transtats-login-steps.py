from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


@given('Launch browser')
def launch(context):
    options = Options()
    options.headless = True
    context.driver = webdriver.Chrome(executable_path='/home/jenkins/.local/bin/chromedriver', options=options)


@when('Open transtats homepage')
def ts_home(context):
    context.driver.get("http://10.65.207.93")
    
@when('Click on login')
def get_login(context):
    context.driver.find_element_by_xpath("/html/body/nav/nav/ul/li[3]/a").click()

@when('Enter username "{usr}" and password "{passwd}"')
def step_impl(context, usr, passwd):
    context.driver.find_element_by_id("id_username").send_keys(usr)
    context.driver.find_element_by_id("id_password").send_keys(passwd)


@when('Click on login button')
def click_login(context):
    context.driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[3]/input").click()

@then('Successful login to the Transtats admin page.')
def admin_page(context):
    try:
        txt = context.driver.find_element_by_xpath('//*[@id="content"]/h1').text
    except:
        assert False, "login failed"
    else:
        if txt == "Site administration":
            assert True, "login success"
        else:
            assert False, "login failed"
    finally:
        context.driver.close()
