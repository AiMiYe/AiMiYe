from selenium_notes.chapter_02.CustomSeleniumUtils import CustomSeleniumUtils
from lxml import etree
from time import sleep
from selenium_notes.utils.tools import conversion_to_elevate


def parse(text, path):
    eles = []
    html = etree.HTML(text)
    rlt = html.xpath(path)
    rlts = [x.strip() for x in rlt]
    for i in rlts:
        if i:
            eles.append(i)
    return eles


def save_csv(content):
    with open(r"./dlt.csv", 'a', encoding="UTF-8") as file:
        # file.write("日期,期数,红球_1,红球_2,红球_3,红球_4,红球_5,红球_6,蓝球_1")
        file.write(content + "\n")


driver = CustomSeleniumUtils()
# driver.open_url("http://kaijiang.zhcw.com/zhcw/html/ssq/list.html")
driver.open_url("https://www.lottery.gov.cn/kj/kjlb.html?dlt")
for _ in range(138):  # 138
    while True:
        ele = driver.find_element_by_invisibility(("xpath", "//a[text()='下一页']"))
        if not ele:
            sleep(5)
            driver.refresh()
        else:
            break
    date = conversion_to_elevate(parse(driver.get_page_source(), "//td[@align='center']/text()"), 2)
    bord = conversion_to_elevate(parse(driver.get_page_source(), "//em/text()"), 7)
    for i in range(len(date)):
        string = ",".join(date[i] + bord[i])
        save_csv(string)
    sleep(5)
    driver.click(("xpath", "//a[text()='下一页']"))

driver.close()
