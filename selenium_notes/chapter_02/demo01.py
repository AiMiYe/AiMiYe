# from selenium import webdriver
# import time
# from selenium_notes.utils.logutils import logger
# 
# # with webdriver.Chrome(executable_path=r"../drivers/chromedriver89.exe") as driver:
# #     name = str(int(time.time())) + ".png"
# #     driver.get("http://localhost/login")
# #     ele = driver.find_element_by_class_name("imgcode")
# #
# #     loc = ele.location
# #     size = ele.size
# #     driver.save_screenshot(name)
# #     left = loc['x']
# #     top = loc['y']
# #     right = loc['x'] + size['width']
# #     bottom = loc['y'] + size['height']
# #     im = Image.open(name)
# #     im = im.crop((left, top, right, bottom))
# #     im.save(name)
# 
# # if __name__ == '__main__':
# #     ex = r"D:\TesseractOCR\tesseract.exe"
# #     pt.pytesseract.tesseract_cmd = ex
# #     img = Image.open("code.png")
# #     print(pt.image_to_string(img, lang="eng"))
# 
# try:
#     logger.info("open chrome.")
#     driver = webdriver.Chrome(executable_path="../drivers/chromedriver89.exe")
#     logger.info("open worker.")
#     driver.get("http://www.baidu.com/")
#     time.sleep(4)
#     logger.info("close chrome.")
#     driver.close()
# except Exception as _:
#     logger.exception("open chrome error.")
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time


def test_57j():
    """expected_conditions模块visibility_of_element_located类"""
    # visibility_of_element_located(locator) 判断某个locator元素是否可见（前提是存在）
    # 可见代表非隐藏、可显示，并且元素的宽和高都大于0
    # 如果定位到就返回WebElement

    driver = webdriver.Chrome(executable_path="../drivers/chromedriver89.exe")
    driver.maximize_window()
    driver.get("https://www.baidu.com")

    print('开始', time.ctime())
    # 传入driver 返回一个WebElement
    print(ec.visibility_of_element_located((By.CSS_SELECTOR, 'input#kw'))(driver))

    # 传入driver 返回一个WebElement 获取tag_name\\获取class属性值
    print(ec.visibility_of_element_located((By.CSS_SELECTOR, 'input#kw'))(driver).get_attribute('class'))
    print('1', time.ctime())

    try:
        print(ec.visibility_of_element_located((By.CSS_SELECTOR, 'input#kw111'))(driver))
    except BaseException as e111:
        print(e111)  # 不存在的元素 报错 Message: no such element: Unable to locate element
    print('2', time.ctime())

    # 和显式等待结合
    print(WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'input#kw')),
                                          '失败'))  # 返回WebElement
    print(WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'input#kw')),
                                          '失败').get_attribute('class'))
    print('3', time.ctime())

    try:

        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'input#kkk1111')), '失败')
    except BaseException as e222:
        print(e222)  # 不存在的元素，显式等待+报错
    print('4', time.ctime())

    time.sleep(1)
    driver.quit()


test_57j()
