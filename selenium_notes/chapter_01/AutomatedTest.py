from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium import webdriver
from PIL import Image
import time


class SecPackage(object):
    """
    基于原生的selenium框架做了二次封装
    """

    def __init__(self, driver):
        """
        启动浏览器参数化，默认启动chrome
        """
        self.__driver = driver
        self.__time_out = 10

    def open_url(self, url, title=None):
        """
        使用get打开url后，最大化窗口，判断title符合预期
        """
        self.__driver.get(url)
        try:
            WebDriverWait(self.__driver, self.__time_out, 1).until(EC.title_contains(title))
        except TimeoutException:
            print(f"open {url} title error")
        except Exception as msg:
            print(f"Error:{msg}")

    def find_element(self, locator):
        """
         定位单个元素
        """
        element = WebDriverWait(self.__driver, self.__time_out, 1).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator):
        """
         定位多个元素
        """
        element = WebDriverWait(self.__driver, self.__time_out, 1).until(EC.presence_of_all_elements_located(locator))
        return element

    def click_element(self, locator):
        """
         定位元素
        """
        element = WebDriverWait(self.__driver, self.__time_out, 1).until(EC.element_to_be_clickable(locator))
        return element

    def click(self, locator):
        """
        点击操作
        """
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        """
         发送文本，清空后输入
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_text_in_element(self, locator, text):
        """
        判断文本在元素里,没定位到元素返回False，定位到返回判断结果布尔值
        """
        try:
            result = WebDriverWait(self.__driver, self.__time_out, 1).until(
                EC.text_to_be_present_in_element(locator, text))
        except self.time_outException:
            print("元素没定位到：" + str(locator))
            return False
        else:
            return result

    def is_text_in_value(self, locator, value):
        """
        判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值
        """
        try:
            result = WebDriverWait(self.__driver, self.__time_out, 1).until(
                EC.text_to_be_present_in_element_value(locator, value))
        except self.time_outException:
            print("元素没定位到：" + str(locator))
            return False
        else:
            return result

    def is_title(self, title):
        """
        判断title完全等于
        """
        result = WebDriverWait(self.__driver, self.__time_out, 1).until(EC.title_is(title))
        return result

    def is_title_contains(self, txt):
        """
        判断title包含txt
        """
        result = WebDriverWait(self.__driver, self.__time_out, 1).until(EC.title_contains(txt))
        return result

    def is_selected(self, locator):
        """
        判断元素被选中，返回布尔值
        """
        result = WebDriverWait(self.__driver, self.__time_out, 1).until(
            EC.element_located_to_be_selected(locator))
        return result

    def is_selected_be(self, locator, selected=True):
        """
        判断元素的状态，selected是期望的参数true/False, 返回布尔值
        """
        result = WebDriverWait(self.__driver, self.__time_out, 1).until(
            EC.element_located_selection_state_to_be(locator, selected))
        return result

    def is_alert_present(self):
        """
        判断页面是否有alert，有返回alert(注意这里是返回alert,不是True)没有返回False
        """
        result = WebDriverWait(self.__driver, self.__time_out, 1).until(EC.alert_is_present())
        return result

    def is_invisibility(self, locator):
        """
        元素可见返回本身，不可见返回True，没找到元素也返回True
        """
        result = WebDriverWait(self.__driver, self.__time_out, 1).until(
            EC.invisibility_of_element_located(locator))
        return result

    def is_clickable(self, locator):
        """
        元素可以点击is_enabled返回本身，不可点击返回Fasle
        """
        result = WebDriverWait(self.__driver, self.__time_out, 1).until(
            EC.element_to_be_clickable(locator))
        return result

    def is_located(self, locator):
        """
        判断元素有没被定位到（并不意味着可见），定位到返回element,没定位到返回False
        """
        result = WebDriverWait(self.__driver, self.__time_out, 1).until(
            EC.presence_of_element_located(locator))
        return result

    def left_click(self, locator):
        """
        鼠标左键单击
        """
        element = self.find_element(locator)
        ActionChains(self.__driver).click(element).perform()

    def l_double_click(self, locator):
        """
        鼠标左键双击
        """
        element = self.find_element(locator)
        ActionChains(self.__driver).double_click(element).perform()

    def right_click(self, locator):
        """
        鼠标右键单击
        """
        element = self.find_element(locator)
        ActionChains(self.__driver).context_click(element).perform()

    def move_to_element(self, locator):
        """
        鼠标悬停操作
        """
        element = self.find_element(locator)
        ActionChains(self.__driver).move_to_element(element).perform()

    def switch_To_Window(self, number):
        """
        跳转浏览器标签,只适用于浏览器只有两个标签
        """
        handles = self.__driver.window_handles
        if len(handles) == 2:
            self.__driver.switch_to.window(handles[number - 1])
        else:
            print('浏览器标签大于2个')

    def implicitly_wait(self):
        """
        隐示等待
        """
        self.__driver.implicitly_wait(self.__time_out)

    def mix_window(self):
        """
        浏览器窗口最大化
        """
        self.__driver.minimize_window()

    def back(self):
        """
        浏览器返回键
        """
        self.__driver.back()

    def forward(self):
        """
        浏览器前进键
        """
        self.__driver.forward()

    def close(self):
        """
        关闭浏览器
        """
        self.__driver.close()

    def quit(self):
        """
        退出浏览器
        """
        self.__driver.quit()

    def get_title(self):
        """
        获取title
        """
        return self.__driver.title

    def get_text(self, locator):
        """
        获取文本
        """
        element = self.find_element(locator)
        return element.text

    def get_cookie(self):
        """
        获取cookies
        """
        return self.__driver.get_cookies()[0]

    def get_attribute(self, locator, name):
        """
        获取属性
        """
        element = self.find_element(locator)
        return element.get_attribute(name)

    def js_execute(self, js):
        """
        执行js
        """
        return self.__driver.execute_script(js)

    def js_focus_element(self, locator):
        """
        聚焦元素
        """
        target = self.find_element(locator)
        self.__driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        """
        滚动到顶部
        """
        js = "window.scrollTo(0,0)"
        self.__driver.execute_script(js)

    def js_scroll_end(self):
        """
        滚动到底部
        """
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.__driver.execute_script(js)

    def select_by_index(self, locator, index):
        """
        通过索引,index是索引第几个，从0开始
        """
        element = self.find_element(locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        """
        通过value属性
        """
        element = self.find_element(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        """
        通过文本值定位
        """
        element = self.find_element(locator)
        Select(element).select_by_visible_text(text)

    def get_capture_screen(self, file_name):
        """
        截取整个浏览器屏幕
        :param file_name: 图片文件保存路径
        :return: Null
        """
        self.__driver.save_screenshot(file_name)

    def get_element_screen(self, locator):
        now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        file_name = f"{locator[1] + now}.png"
        self.__driver.save_screenshot(file_name)
        element = self.find_element(locator)
        left = element.location['x']
        top = element.location['y']
        right = element.location['x'] + element.size['width']
        bottom = element.location['y'] + element.size['height']

        im = Image.open(file_name)
        im = im.crop((left, top, right, bottom))
        im.save(file_name)


if __name__ == '__main__':
    l = ("id", "kw")
    d = webdriver.Chrome(executable_path="../drivers/chromedriver89.exe")
    d.get("https://www.baidu.com")
    ins = SecPackage(d)
    ins.get_element_screen(l)
    ins.quit()
