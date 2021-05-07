from selenium import webdriver
import time
from PIL import Image
import pytesseract

# with webdriver.Chrome(executable_path=r"../drivers/chromedriver89.exe") as driver:
#     name = str(int(time.time())) + ".png"
#     driver.get("http://localhost/login")
#     ele = driver.find_element_by_class_name("imgcode")
#
#     loc = ele.location
#     size = ele.size
#     driver.save_screenshot(name)
#     left = loc['x']
#     top = loc['y']
#     right = loc['x'] + size['width']
#     bottom = loc['y'] + size['height']
#     im = Image.open(name)
#     im = im.crop((left, top, right, bottom))
#     im.save(name)

if __name__ == '__main__':
    st = pytesseract.image_to_string("E:/PyFiles/selenium_notes/chapter_02/1620396175.png")
    print(st)
