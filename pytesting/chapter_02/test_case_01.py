import pytest
from selenium import webdriver

"""
@pytest.fixture参数：
    scope: 
"""


@pytest.fixture(scope="module")
def open_chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_open_baidu(open_chrome):
    open_chrome.get("http://www.baidu.com/")
    assert "百度" in open_chrome.title


# @pytest.mark.usefixtures('open_chrome') 注意：使用此方法调用fixture不能拿到fixture的返回值
def test_open_sogou(open_chrome):
    open_chrome.get("https://www.sogou.com/")
    assert "搜狗" in open_chrome.title


if __name__ == '__main__':
    pytest.main(['test_case_01.py'])
