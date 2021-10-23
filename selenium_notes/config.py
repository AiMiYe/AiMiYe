import os
import sys

sys.path.append(os.path.split(os.path.dirname(__file__))[0])

# 项目根目录
ROOT = os.path.dirname(os.path.abspath(__file__))

# 驱动程序路径
CHROME_DRIVER = os.path.join(ROOT, "drivers", "chromedriver.exe")
FIREFOX_DRIVER = os.path.join(ROOT, "drivers", "geckodriver.exe")
EDGE_DRIVER = os.path.join(ROOT, "drivers", "msedgedriver.exe")

# 日志目录
LOG = os.path.join(ROOT, "logs")
CHROME_SERVICE_LOG = os.path.join(LOG, "chrome.log")
FIREFOX_SERVICE_LOG = os.path.join(LOG, "firefox.log")
EDGE_SERVICE_LOG = os.path.join(LOG, "edge.log")

# ini数据文件目录
ELEMENT = os.path.join(ROOT, "data", 'element.ini')

# json数据文件目录
JSON = os.path.join(ROOT, "data", 'winter.json')

# 图片文件目录
IMG = os.path.join(ROOT, 'image')
