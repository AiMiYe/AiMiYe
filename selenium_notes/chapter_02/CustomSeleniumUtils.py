from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium_notes.utils.logUtils import logger
from selenium.common.exceptions import *
from selenium_notes.config import *
from selenium import webdriver
from time import sleep
from PIL import Image
import os


class CustomSeleniumUtils(object):
    def __init__(self, browser):
        self.__browser = browser
        self.__timeout = 10  # 超时时间, 单位：S

    def find_element_by_presence(self, locator: tuple) -> WebElement:
        """
        定位单个元素是否已加载到DOM树中
        :param locator: 元素定位器, 数据类型：元组. 如：('id', 'kw')
        :return: 元素对象
        """
        try:
            ele = WebDriverWait(self.__browser, self.__timeout, 1).until(EC.presence_of_element_located(locator))
            logger.info(f"element {locator} positioning succeeded")
            return ele
        except TimeoutException as _:
            logger.exception("element positioning error")

    def find_element_by_invisibility(self, locator: tuple) -> WebElement:
        """
        定位单个元素是否在浏览器页面中可见, 即：元素的宽度与高度大于0
        :param locator: 元素定位器, 数据类型：元组. 如：('id', 'kw')
        :return: 元素对象
        """
        try:
            ele = WebDriverWait(self.__browser, self.__timeout, 1).until(EC.visibility_of_element_located(locator))
            logger.info(f"element {locator} positioning succeeded")
            return ele
        except TimeoutException as _:
            logger.exception(f"element positioning error")

    def max_window(self) -> None:
        """
        浏览器窗口最大化
        :return:
        """
        self.__browser.maximize_window()
        logger.info("maximize the browser window")

    def min_window(self) -> None:
        """
        浏览器窗口最小化
        :return:
        """
        self.__browser.minimize_window()
        logger.info("minimize the browser window")

    def set_window_size(self, size: tuple) -> None:
        """
        设置当前浏览器宽度与高度
        :param size: (宽度, 高度)
        :return:
        """
        self.__browser.set_window_size(*size)
        logger.info("set the current browser width and height")

    def set_window_position(self, position: tuple) -> None:
        """
        设置浏览器左上角的点在屏幕中的位置
        :param position: (x, y)
        :return:
        """
        self.__browser.set_window_position(*position)
        logger.info("set the position of browser in the screen")

    def refresh(self) -> None:
        """
        刷新浏览器窗口
        :return:
        """
        self.__browser.refresh()
        logger.info("refresh the browser window")

    def forward(self) -> None:
        """
        浏览器前进
        :return:
        """
        self.__browser.forward()
        logger.info("browser forward")

    def back(self) -> None:
        """
        浏览器后退
        :return:
        """
        self.__browser.back()
        logger.info("browser back")

    def get_page_source(self) -> str:
        """
        获取当前页面源码
        :return:
        """
        logger.info("get the page source")
        return self.__browser.page_source


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER, service_log_path=CHROME_SERVICE_LOG)
    loc = ("id", 'kw')
    driver.get("https://www.baidu.com/")
    cu = CustomSeleniumUtils(driver)
    cu.max_window()
    cu.refresh()
    sleep(5)
    driver.quit()
