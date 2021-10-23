import os
import time
from time import sleep

from PIL import Image
from selenium import webdriver
from selenium_notes.config import *
from selenium.common.exceptions import *
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium_notes.utils.logUtils import logger


class CustomSeleniumUtils(object):
    __error_code = "browser object initialization exception"

    def __init__(self, browser="edge"):
        self._timeout = 30  # 超时时间, 单位：S
        try:
            if browser.upper() == "CHROME":
                self._driver = webdriver.Chrome(executable_path=CHROME_DRIVER, service_log_path=CHROME_SERVICE_LOG)
            elif browser.upper() == "FIREFOX":
                self._driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER, service_log_path=FIREFOX_SERVICE_LOG)
            else:
                self._driver = webdriver.Edge(executable_path=EDGE_DRIVER, service_log_path=EDGE_SERVICE_LOG)
            logger.info(f"the {browser} object was initialized successfully")
        except Exception as _:
            logger.exception("browser startup failed")

    def open_url(self, url: str):
        """
        访问网址
        :param url:
        :return:
        """
        self._driver.get(url)
        logger.info(f"Visit {url}")

    def find_element_by_presence(self, locator: tuple) -> WebElement:
        """
        定位单个元素是否已加载到DOM树中
        :param locator: 元素定位器, 数据类型：元组. 如：('id', 'kw')
        :return: 元素对象
        """
        try:
            ele = WebDriverWait(self._driver, self._timeout, 1).until(EC.presence_of_element_located(locator))
            logger.info(f"element {locator} positioning succeeded")
            return ele
        except TimeoutException as _:
            logger.exception("element positioning error")
        except Exception as _:
            logger.exception(CustomSeleniumUtils.__error_code)

    def find_element_by_invisibility(self, locator: tuple) -> WebElement:
        """
        定位单个元素是否在浏览器页面中可见, 即：元素的宽度与高度大于0
        :param locator: 元素定位器, 数据类型：元组. 如：('id', 'kw')
        :return: 元素对象
        """
        try:
            ele = WebDriverWait(self._driver, self._timeout, 1).until(EC.visibility_of_element_located(locator))
            logger.info(f"element {locator} positioning succeeded")
            return ele
        except TimeoutException as _:
            logger.exception(f"element positioning error")
        except Exception as _:
            logger.exception(CustomSeleniumUtils.__error_code)

    def input_value(self, locator: tuple, text: str) -> None:
        """
        输入框输入文本
        :param locator: 元素定位器
        :param text: 文本值
        :return:
        """

        element = self.find_element_by_invisibility(locator)
        element.clear()
        logger.info("wipe data")
        element.send_keys(text)
        logger.info(f"element {locator} input text {text}")

    def click(self, locator: tuple) -> None:
        """
        点击元素
        :param locator:
        :return:
        """

        self.find_element_by_invisibility(locator).click()
        logger.info(f"Click on the {locator} element")

    @staticmethod
    def stop(seconds: int):
        """
        睡眠时间
        :param seconds:
        :return:
        """
        sleep(seconds)
        logger.info(f"Threads sleep for {seconds} seconds")

    def max_window(self) -> None:
        """
        浏览器窗口最大化
        :return:
        """

        self._driver.maximize_window()
        logger.info("maximize the browser window")

    def min_window(self) -> None:
        """
        浏览器窗口最小化
        :return:
        """

        self._driver.minimize_window()
        logger.info("minimize the browser window")

    def set_window_size(self, size: tuple) -> None:
        """
        设置当前浏览器宽度与高度
        :param size: (宽度, 高度)
        :return:
        """

        self._driver.set_window_size(*size)
        logger.info("set the current browser width and height")

    def set_window_position(self, position: tuple) -> None:
        """
        设置浏览器左上角的点在屏幕中的位置
        :param position: (x, y)
        :return:
        """

        self._driver.set_window_position(*position)
        logger.info("set the position of browser in the screen")

    def refresh(self) -> None:
        """
        刷新浏览器窗口
        :return:
        """

        self._driver.refresh()
        logger.info("refresh the browser window")

    def forward(self) -> None:
        """
        浏览器前进
        :return:
        """

        self._driver.forward()
        logger.info("browser forward")

    def back(self) -> None:
        """
        浏览器后退
        :return:
        """

        self._driver.back()
        logger.info("browser back")

    def get_page_source(self) -> str:
        """
        获取当前页面源码
        :return:
        """

        logger.info("get the page source")
        return self._driver.page_source

    def quit(self) -> None:
        """
        退出浏览器
        :return:
        """

        self._driver.quit()
        logger.info("exit browser")

    def close(self) -> None:
        """
        关闭浏览器当前table页
        :return:
        """

        self._driver.close()
        logger.info("close the current table page of the browser")

    def get_all_cookies(self) -> list:
        """
        获取所有cookies
        :return: [{cookie_1},{cookie_2}]
        """

        cookies = self._driver.get_cookies()
        logger.info(f"get all cookies: {cookies}")
        return cookies

    def get_cookie(self, name: str) -> dict:
        """
        获取指定cookie
        :param name: cookie名称
        :return: dict
        """

        cookie = self._driver.get_cookie(name)
        logger.info(f"get cookie name: {name} value: {cookie}")
        return cookie

    def set_cookie(self, cookie: dict) -> None:
        """
        设置cookie
        :param cookie: dict
        :return:
        """

        self._driver.add_cookie(cookie)
        logger.info(f"set cookie: {cookie}")

    def delete_all_cookies(self) -> None:
        """
        删除所有cookie
        :return:
        """

        self.get_all_cookies()
        self._driver.delete_all_cookies()
        logger.info(f"delete all cookies")

    def delete_cookie(self, cookie) -> None:
        """
        删除指定cookie
        :param cookie:
        :return:
        """

        self.get_cookie(cookie)
        self._driver.delete_cookie(cookie)
        logger.info(f"delete cookie: {cookie}")

    def get_current_url(self) -> str:
        """
        获取当前URL
        :return:
        """

        self.stop(1)
        url = self._driver.current_url
        logger.info(f"url: {url}")
        return url

    def get_current_window_handle(self) -> str:
        """
        获取当前浏览器table页句柄
        :return:
        """

        handle = self._driver.current_window_handle
        logger.info(f"handle: {handle}")
        return str(handle)

    def get_all_window_handles(self) -> list:
        """
        获取当前浏览器所有table页句柄
        :return:
        """

        handles = self._driver.window_handles
        logger.info(f"handles: {handles}")
        return handles

    def switch_to_window_handle(self, index: int) -> None:
        """
        切换到指定浏览器table页
        :param index: 从0开始的table索引
        :return:
        """

        handle = int(index)
        handles = self.get_all_window_handles()
        self._driver.switch_to.window(handles[handle])
        logger.info(f"switch to {handles[handle]} window handle")

    def auto_switch_to_window_handle(self) -> None:
        """
        如果浏览器句柄有且仅有2个，自动切换为另一个
        :return:
        """

        handles = self.get_all_window_handles()
        if len(handles) != 2:
            logger.info(f"handles length is not equal to 2 handles: {handles}")
            return
        for i in handles:
            if i != self.get_current_window_handle():
                self._driver.switch_to.window(i)

    def save_screenshot_as_file(self, file_name: str) -> None:
        """
        保存当前浏览器屏幕为png格式图片
        :param file_name: png文件路径
        :return:
        """

        rlt = self._driver.save_screenshot(file_name)
        if rlt:
            logger.info("the screenshot file was saved successfully")
        else:
            logger.info("failed to save screenshot file")

    def save_screenshot_as_base64(self) -> str:
        """
        保存当前浏览器屏幕为base64编码的字符串
        :return:
        """

        img = self._driver.get_screenshot_as_base64()
        logger.info(f"base64: {img}")
        return img

    def save_element_screenshot_as_file(self, locator: tuple, image_path: str):
        """
        截取并保存屏幕中元素的图片
        :param locator:
        :param image_path:
        :return:
        """

        if not os.path.exists(image_path):
            os.mkdir(image_path)
        file = os.path.join(image_path, f"{time.strftime('%Y%m%d%H%M%S', time.localtime())}.png")
        ele = os.path.join(image_path, f"{locator[0]}_{locator[1]}_{time.strftime('%H%M%S', time.localtime())}.png")
        self.save_screenshot_as_file(file)
        element = self.find_element_by_invisibility(locator)

        location = element.location
        logger.info(f"get element: {locator} position")
        size = element.size
        logger.info(f"get element: {locator} size")
        left = location['x']
        logger.info(f"left: {left}")
        top = location['y']
        logger.info(f"top: {top}")
        right = left + size['width']
        logger.info(f"right: {right}")
        bottom = top + size['height']
        logger.info(f"bottom: {bottom}")
        im = Image.open(file)
        im = im.crop((left, top, right, bottom))
        im.save(ele)

    def execute_script(self, script: str) -> str:
        """
        执行JavaScript脚本
        :param script:
        :return:
        """

        rlt = self._driver.execute_script(script)
        if rlt:
            return rlt
        return self._driver.execute_script(script)

    def _switch_to_alert(self) -> Alert:
        """
        等待alert出现，并且切换进去
        :return:
        """

        alert = WebDriverWait(self._driver, self._timeout, 1).until(EC.alert_is_present())
        logger.info("switch to alert")
        return alert

    def alert_dismiss(self) -> None:
        """
        取消Alert弹窗
        :return:
        """
        alert = self._switch_to_alert()
        alert.dismiss()
        logger.info("cancel alert")

    def alert_accept(self) -> None:
        """
        确定Alert弹窗
        :return:
        """
        alert = self._switch_to_alert()
        alert.accept()
        logger.info("determine alert")

    def get_alert_text(self) -> str:
        """
        获取Alert弹窗内容文本
        :return:
        """
        alert = self._switch_to_alert()
        logger.info(f"get alert text: {alert}")
        return alert.text

    def alert_send_keys(self, text: str) -> None:
        """
        Alert弹窗中输入内容
        :param text:
        :return:
        """
        alert = self._switch_to_alert()
        alert.send_keys(text)
        logger.info(f"input text: {text} in alert")

    def switch_to_iframe(self, locator: tuple) -> None:
        """
        切换至指定的iframe/frame
        :param locator: iframe元素定位器
        :return:
        """

        rlt = WebDriverWait(self._driver, self._timeout, 1).until(
            EC.frame_to_be_available_and_switch_to_it(locator))
        if rlt:
            logger.info(f"switch to iframe: {locator}")
        else:
            logger.info(f"switch to iframe failure")

    def switch_to_parent_frame(self) -> None:
        """
        切换至上一层级iframe/frame
        :return:
        """

        self._driver.switch_to.parent_frame()
        logger.info("switch to parent frame")

    def switch_out_all_iframe(self) -> None:
        """
        切换出所有层级的iframe/frame
        :return:
        """

        self._driver.switch_to.default_content()
        logger.info("switch out all iframe")

    def mouse_left_click(self, locator) -> None:
        element = self.find_element_by_invisibility(locator)
        ActionChains(self._driver).click(element).perform()
        logger.info(f"mouse left click element: {locator}")

    def mouse_right_click(self, locator) -> None:
        element = self.find_element_by_invisibility(locator)
        ActionChains(self._driver).context_click(element).perform()
        logger.info(f"mouse right click element: {locator}")

    def mouse_left_double_click(self, locator) -> None:
        element = self.find_element_by_invisibility(locator)
        ActionChains(self._driver).double_click(element).perform()
        logger.info(f"mouse left double click element: {locator}")

    def mouse_move_to_element(self, locator) -> None:
        pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.quit()
