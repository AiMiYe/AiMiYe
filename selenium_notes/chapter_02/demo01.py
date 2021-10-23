
from selenium_notes.config import *
from selenium_notes.utils.handle_ini import HandleIni
from selenium_notes.chapter_02.CustomSeleniumUtils import CustomSeleniumUtils


def one():
    with CustomSeleniumUtils(browser="firefox") as driver:
        ini = HandleIni(ELEMENT)
        # locator = ini.get_section_all_values("ruoyi_login")
        # driver.max_window()

        # driver.open_url("http://192.168.223.135/ruoyi/login")
        # driver.input_value(locator.get("username_box"), "admin")
        # driver.input_value(locator.get("password_box"), "admin123")
        # driver.click(locator.get("login_button"))
        # driver.stop(5)
        # driver.auto_switch_to_window_handle()
        # driver.stop(5)
        # locator = ini.get_section_all_values("baidu")
        driver.open_url(f"file:///E:/PyFiles/selenium_notes/html/text.html")
        driver.max_window()
        driver.input_value(("id", "kw"), "selenium")
        driver.mouse_left_double_click(("id", "kw"))
        driver.stop(3)


if __name__ == '__main__':
    one()
