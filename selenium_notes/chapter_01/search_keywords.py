from selenium import webdriver
import time

# http://sahitest.com/demo/index.htm
with webdriver.Chrome(executable_path=r"../drivers/chromedriver89.exe") as driver:
    driver.get("https://www.baidu.com/")
    time.sleep(2)
    # driver.find_element_by_id("kw").send_keys("selenium")
    # time.sleep(2)
    # driver.find_element_by_id("su").click()
    focus = 'document.querySelector("#kw").value("selenium")'

    driver.execute_script(focus)
    blur = 'document.querySelector("#kw").blur()'
    # driver.execute_script(focus)
    time.sleep(10)
