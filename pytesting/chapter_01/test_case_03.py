import pytest
from selenium import webdriver

"""
pytest参数化：
    当一组测试用例有相似的测试步骤时，就可以通过参数化的方式简化测试用例的编写。
    通过装饰器 @pytest.mark.parametrize() 来设置参数
        参数说明：
            argnames：指定参数名称。类型: ('arg1','arg2','arg3')、['arg1','arg2','arg3']、"arg1,arg2,arg3"
            argvalues: 与参数名称对应的参数值。类型: (("val1","val2","val3"),("val4","val5","val6"))
                                                [["val1","val2","val3"],["val4","val5","val6"]]
            ids: 设置测试用例名称，默认None
"""


@pytest.mark.parametrize(['url', 'exp'],
                         (('http://www.baidu.com/', '百度'),
                          ('https://www.sogou.com/', '搜狗'),
                          ('https://www.so.com/', '360')),
                         ids=['测试百度搜索', '测试搜索搜索', '测试360搜索'])
def test_open_search_page(url, exp):
    driver = webdriver.Chrome()
    driver.get(url)
    title = driver.title
    driver.quit()
    assert exp in title


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case_03.py', '-n', '3'])
    # pytest.main(['-s', '-v', 'test_case_03.py'])
