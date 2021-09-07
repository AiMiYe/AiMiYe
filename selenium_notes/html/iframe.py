from selenium_notes.config import *
from selenium import webdriver


def twe():
    with webdriver.Firefox(executable_path=FIREFOX_DRIVER, service_log_path=FIREFOX_SERVICE_LOG) as driver:
        driver.get(r"E:\PyFiles\selenium_notes\chapter_02\iframe.html")
        print(driver.find_element_by_id("p1").text)
        driver.switch_to.frame(driver.find_element_by_id("one"))
        print(driver.find_element_by_id("p2").text)
        driver.switch_to.frame(driver.find_element_by_id("twe"))
        print(driver.find_element_by_id("p3").text)
        driver.switch_to.default_content()
        print(driver.find_element_by_id("p1").text)


if __name__ == '__main__':
    twe()
