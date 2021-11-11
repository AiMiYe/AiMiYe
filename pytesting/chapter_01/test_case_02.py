# 测试断言
import pytest
from selenium import webdriver


def test_title_is_successful():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com/")
    title = driver.title
    driver.quit()
    assert "百度" in title


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case_02.py'])
