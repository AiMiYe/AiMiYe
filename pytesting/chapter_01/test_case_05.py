import pytest

"""
测试函数级别
    setup_module/teardown_module: 在py文件执行之前/之后执行
    setup_function/teardown_function: 在每一个测试测试函数执行之前/之后执行
    setup/teardown: 在每一个测试用例执行之前/之后执行
"""


def setup_module():
    print(f"==========setup_module==========")


def teardown_module():
    print(f"========teardown_module=========")


def setup_function():
    print(f"+++++++++setup_function+++++++++")


def teardown_function():
    print(f"+++++++teardown_function++++++++")


def setup():
    print(f"-----------setup------------")


def teardown():
    print(f"----------teardown----------")


def test_case_01():
    print("<-test_case_01->")
    assert 1 == 1


def test_case_02():
    print("<-test_case_02->")
    assert 1 == 2


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case_05.py'])
