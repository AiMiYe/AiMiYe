import pytest

"""
使用一下方法调用fixture, 执行顺序是由下往上执行
@pytest.mark.usefixtures("fixture_01")
@pytest.mark.usefixtures("fixture_02")
@pytest.mark.usefixtures("fixture_03")
def test_case():
    print("执行测试用例：test_case")
    
"""


@pytest.fixture()
def fixture_01():
    print("----------fixture_01----------")


@pytest.fixture()
def fixture_02():
    print("==========fixture_02==========")


@pytest.fixture()
def fixture_03():
    print("\n++++++++++fixture_03++++++++++")


@pytest.mark.usefixtures("fixture_01")
@pytest.mark.usefixtures("fixture_02")
@pytest.mark.usefixtures("fixture_03")
def test_case():
    print("执行测试用例：test_case")


if __name__ == '__main__':
    pytest.main(['test_case_04.py'])
