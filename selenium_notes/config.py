import os

# 项目根目录
ROOT = os.path.dirname(os.path.abspath(__file__))

# 驱动程序路径
CHROME_DRIVER = os.path.join(ROOT, "drivers", "chromedriver89.exe")
FIREFOX_DRIVER = os.path.join(ROOT, "drivers", "geckodriver.exe")
EDGE_DRIVER = os.path.join(ROOT, "drivers", "msedgedriver90.exe")

# 日志目录
LOG = os.path.join(ROOT, "logs")
CHROME_SERVICE_LOG = os.path.join(LOG, "chrome.log")
FIREFOX_SERVICE_LOG = os.path.join(LOG, "firefox.log")
EDGE_SERVICE_LOG = os.path.join(LOG, "edge.log")
