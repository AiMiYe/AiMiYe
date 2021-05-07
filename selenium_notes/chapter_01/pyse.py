from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Pyse(object):
    def __init__(self, browser='chrome'):  # 初始化driver
        if browser == "firefox" or browser == "ff":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            option = webdriver.ChromeOptions()
            option.add_argument("--start-maximized")
            driver = webdriver.Chrome(chrome_options=option)
        elif browser == "internet explorer" or browser == "ie":
            driver = webdriver.Ie()
        elif browser == "opera":
            driver = webdriver.Opera()
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        elif browser == 'edge':
            driver = webdriver.Edge()
        try:
            self.driver = driver
        except Exception:
            raise NameError(
                "Not found %s browser,You can enter 'ie', 'ff', 'opera', 'phantomjs', 'edge' or 'chrome'." % browser)

    def element_wait(self, css, secs=5):  # 等待元素出现，显示等待
        """
        Waiting for an element to display.

        Usage:
        driver.element_wait("css=>#el",10)
        """
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_all_elements_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")

    def get_element(self, css):  # 获取元素
        '''
        Judge element positioning way, and returns the element.
        '''
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "class":
            element = self.driver.find_element_by_class_name(value)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    def open(self, url):  # 打开目标网址
        '''
        open url.

        Usage:
        driver.open("https://www.baidu.com")
        '''
        self.driver.get(url)

    def max_window(self):  # 窗口最大化展示
        '''
        Set browser window maximized.

        Usage:
        driver.max_window()
        '''
        self.driver.maximize_window()

    def set_window(self, wide, high):  # 设置窗口宽和高
        '''
        Set browser window wide and high.

        Usage:
        driver.set_window(wide,high)
        '''
        self.driver.set_window_size(wide, high)

    def type(self, css, text):  # 往文本框输入字符串
        '''
        Operation input box.

        Usage:
        driver.type("css=>#el","selenium")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.send_keys(text)

    def clear(self, css):  # 清除字符串
        '''
        Clear the contents of the input box.

        Usage:
        driver.clear("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.clear()

    def click(self, css):  # 点击操作
        '''
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.click()

    def right_click(self, css):  # 右击操作
        '''
        Right click element.

        Usage:
        driver.right_click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, css):  # 鼠标悬浮
        '''
        Mouse over the element.

        Usage:
        driver.move_to_element("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, css):  # 双击
        '''
        Double click element.

        Usage:
        driver.double_click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, el_css, ta_css):  # 拖拽操作，拼图
        '''
        Drags an element a certain distance and then drops it.

        Usage:
        driver.drag_and_drop("css=>#el","css=>#ta")
        '''
        self.element_wait(el_css)
        element = self.get_element(el_css)
        self.element_wait(ta_css)
        target = self.get_element(ta_css)
        ActionChains(driver).drag_and_drop(element, target).perform()

    def click_text(self, text):
        '''
        Click the element by the link text

        Usage:
        driver.click_text("新闻")
        '''
        self.driver.find_element_by_partial_link_text(text).click()

    def close(self):  # 关闭当前浏览器
        '''
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.

        Usage:
        driver.close()
        '''
        self.driver.close()

    def quit(self):  # 关闭所有浏览器
        '''
        Quit the driver and close all the windows.

        Usage:
        driver.quit()
        '''
        self.driver.quit()

    def submit(self, css):  # 提交操作
        '''
        Submit the specified form.

        Usage:
        driver.submit("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.submit()

    def F5(self):  # 按钮刷新
        '''
        Refresh the current page.

        Usage:
        driver.F5()
        '''
        self.driver.refresh()

    def js(self, script):  # 执行js
        '''
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        '''
        self.driver.execute_script(script)

    def get_attribute(self, css, attribute):  # 获取属性
        '''
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("css=>#el","type")
        '''
        el = self.get_element(css)
        return el.get_attribute(attribute)

    def get_text(self, css):
        '''
        Get element text information.

        Usage:
        driver.get_text("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        return el.text

    def get_display(self, css):
        '''
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        return el.is_displayed()

    def get_title(self):
        '''
        Get window title.

        Usage:
        driver.get_title()
        '''
        return self.driver.title

    def get_url(self):
        '''
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        '''
        return self.driver.current_url

    def get_windows_img(self, file_path):  # 截图
        '''
        Get the current window screenshot.

        Usage:
        driver.get_windows_img()
        '''
        self.driver.get_screenshot_as_file(file_path)

    def wait(self, secs):
        '''
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        '''
        self.driver.implicitly_wait(secs)

    def accept_alert(self):  # 确认操作
        '''
        Accept warning box.

        Usage:
        driver.accept_alert()
        '''
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):  # 取消操作
        '''
        Dismisses the alert available.

        Usage:
        driver.dismiss_alert()
        '''
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, css):  # 向下跳一层
        '''
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("css=>#el")
        '''
        self.element_wait(css)
        iframe_el = self.get_element(css)
        self.driver.switch_to.frame(iframe_el)

    def switch_to_frame_out(self):  # 跳到最外层
        '''
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        '''
        self.driver.switch_to.default_content()

    def open_new_window(self, css):  # 打开新窗口
        '''
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window()
        '''
        original_windows = self.driver.current_window_handle
        el = self.get_element(css)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver.switch_to.window(handle)

    # def _save_png(self, name):
    #     self.get_windows_img(name)

    def wait_and_save_exception(self, css, name):  # 等待并保存异常
        try:
            self.element_wait(css, secs=5)
            print(name)
            return True
        except Exception as e:
            from lib.core.path import PICTUREPATH
            name = PICTUREPATH + name + '.jpg'
            print(name)
            self.get_windows_img(name)
            return False

    def wait_and_exception(self, css):
        try:
            self.element_wait(css, secs=10)
            return True
        except Exception as e:
            return False

    def select_by_value(self, css, value):  # 下拉框操作
        self.element_wait(css)
        el = self.get_element(css)
        Select(el).select_by_value(value)


if __name__ == '__main__':
    driver = Pyse("chrome")  # 打开一个chrome浏览器
