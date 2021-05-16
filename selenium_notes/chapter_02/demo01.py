from selenium import webdriver
import time
from PIL import Image
import pytesseract as pt

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
    ex = r"D:\TesseractOCR\tesseract.exe"
    pt.pytesseract.tesseract_cmd = ex
    img = Image.open("code.png")
    print(pt.image_to_string(img, lang="eng"))
