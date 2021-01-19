from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
import allure

driver = webdriver.Chrome('../../chromedriver/chromedriver.exe')
driver.get('http://guanjia.20783378.com/#/login')

@allure.feature('配置设备UI自动化')
class Test_info:

    @allure.severity('critical')
    @allure.story('用户登录')
    def test_login(self):
        input_ID = driver.find_element_by_xpath("//input[contains(@tabindex,'1')]")
        input_ID.send_keys('13800010001')
        time.sleep(2)
        input_PW = driver.find_element_by_xpath("//input[@type='password']")
        input_PW.send_keys('123456')
        time.sleep(1)
        button_DL = driver.find_element_by_xpath('//button[@type="button"][2]')
        button_DL.click()
        time.sleep(4)

