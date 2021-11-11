import pytest

"""
同一个fixture返回多个参数
"""


@pytest.fixture()
def return_user_pwd():
    return "root", "admin123456"


def test_login(return_user_pwd):
    user_name, password = return_user_pwd
    print(f"user_name: {user_name}")
    print(f"password: {password}")
    assert user_name == "root"
    assert password == "admin123456"


if __name__ == '__main__':
    pytest.main(["test_case_02.py"])
