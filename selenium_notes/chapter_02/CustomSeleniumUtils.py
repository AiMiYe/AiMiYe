from selenium import webdriver
from time import sleep


class CustomSeleniumUtils(object):
    def __init__(self, browser):
        self.__browser = browser
        self.__timeout = 10


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="../drivers/chromedriver89.exe")
    sleep(3)
    driver.quit()
