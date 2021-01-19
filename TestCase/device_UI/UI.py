from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
import allure

def input_demo(a):
    input_el = driver.find_element_by_xpath("//input[contains(@tabindex,'1')]")
    input_el.send_keys('13800010001')
    time.sleep(2)
    # input_el.clear()
    # time.sleep(2)
    input_dl2 = driver.find_element_by_xpath("//input[contains(@type,'password')]")
    # input_dl2.click()
    input_dl2.send_keys('123456')
    time.sleep(2)
    DJ_mm = driver.find_element_by_class_name('show-pwd')
    DJ_mm.click()
    time.sleep(2)
    DJ_dl = driver.find_element_by_xpath('//button')
    DJ_dl.click()

    time.sleep(3)

def test_login1(a):
    input_ID = driver.find_element_by_xpath("//input[contains(@tabindex,'1')]")
    input_ID.send_keys('13800010001')
    time.sleep(2)
    input_PW = driver.find_element_by_xpath("//input[@type='password']")
    input_PW.send_keys('123456')
    time.sleep(1)
    button_DL = driver.find_element_by_xpath('//button[@type="button"][2]')
    button_DL.click()
    time.sleep(4)

if __name__ == '__main__':
    driver = webdriver.Chrome('../../chromedriver/chromedriver.exe')
    driver.get('http://guanjia.20783378.com/#/login')
    test_login1(driver)
    driver.quit()
    pass
