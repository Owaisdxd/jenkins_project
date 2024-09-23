#wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.9/allure-commandline-2.13.9.tgz
#ls -ltrh
#tar -xzf allure-commandline-2.13.9.tgz
#sudo mv allure-2.13.9 /opt/allure
#sudo ln -s /opt/allure/bin/allure /usr/local/bin/allure
#allure --version
#source ~/.bashrc
#pip install allure-pytest
#python -m pytest allure_report.py --alluredir='./allure_report'
# allure serve /home/os/PycharmProjects/project/pytest/pytest_allure_report/allure_report
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def setup_function():
    global driver
    driver=webdriver.Chrome()
    driver.get('https://stage.alnafi.com')
    driver.maximize_window()

def teardown_function():
    global driver
    time.sleep(5)
    driver.quit()

def cred():
    return [
        ('username1@email.com','passone'),
        ('804awias@email.com','passtwo'),
        ('owaidxd2@email.com','passtwo'),
    ]

@pytest.mark.parametrize("username,password",cred()) #using multiple parameters
def test_website(username,password):

    time.sleep(1)
    print("Work is done")
    driver.maximize_window()
    # driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
    # driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    # time.sleep(2)
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(),name="report",attachment_type=AttachmentType.PNG)

#Note you need to run below command to access the report
# python -m pytest filename --alluredir  dir-name(path to allure reports folder)
# allure serve allure-dir-path
