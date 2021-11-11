import pytest

"""
同一个测试用例使用多个fixture
"""


@pytest.fixture()
def return_account():
    return "root"


@pytest.fixture()
def return_pwd():
    return "admin123456"


def test_login(return_account, return_pwd):
    print(f"user_name: {return_account}")
    print(f"password: {return_pwd}")
    assert return_account == "root"
    assert return_pwd == "admin123456"


if __name__ == '__main__':
    pytest.main(["test_case_03.py"])
