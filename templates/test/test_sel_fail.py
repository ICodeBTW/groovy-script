#Implementation of Selenium test automation for this Selenium Python Tutorial
import re
import os
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
# from selenium.webdriver.support.relative_locator import By


# import org.openqa.selenium.chrome.ChromeOptions;
 

from time import sleep

@pytest.fixture()
def chrome_driver():
    options = Options()
    options.add_argument("headless")
    chrome_driver_ = webdriver.Chrome(executable_path="resources/chromedriver",options=options)
    file = os.path.abspath("success-email.html")
    chrome_driver_.get(file)
    chrome_driver_.maximize_window()
    chrome_driver_.fullscreen_window()
    chrome_driver_.save_screenshot('fe.png')
    yield chrome_driver_
    chrome_driver_.close()

def test_Title_Colours_Success(chrome_driver):
        # table_section=chrome_driver.find_element(By.CSS_SELECTOR,".tr-title")
        table_section = chrome_driver.find_element_by_css_selector(".tr-title")
        table_title_backgroundcolor = table_section.value_of_css_property("background-color")
        color = Color.from_string(table_title_backgroundcolor).hex
        print(color)    
        assert color == '#e74c3c'
def test_Number_of_tables(chrome_driver):
        # tables = len(chrome_driver.find_elements(By.XPATH,'//table'))
        tables = len(chrome_driver.find_elements_by_xpath('//table'))
        assert tables == 3
def test_build_url(chrome_driver):
        # urlEle = chrome_driver.find_element(By.PARTIAL_LINK_TEXT,"http://192.168.60.128:8080/job/groovy-script/")
        urlEle = chrome_driver.find_elements_by_partial_link_text("http://192.168.60.128:8080/job/groovy-script/")
        assert "http://192.168.60.128:8080/job/groovy-script/" in urlEle.get_property("href")
# def test_zephyr_url(chrome_driver):
#         urlEle = chrome_driver.find_element(By.PARTIAL_LINK_TEXT,"http://192.168.60.128:8080/job/groovy-script/")
#         assert "http://192.168.60.128:8080/job/groovy-script/" in urlEle.get_property("href")
# def test_sqube_url(chrome_driver):
#         urlEle = chrome_driver.find_element(By.PARTIAL_LINK_TEXT,"http://192.168.60.128:8080/job/groovy-script/")
#         assert "http://192.168.60.128:8080/job/groovy-script/" in urlEle.get_property("href")
 
# if __name__ == '__main__':
#     Suc = TestSuccessMail()
#     Suc.Test_Title_Colours_Success()
#     Suc.Test_Number_of_tables()
#     Suc.Test_build_url()