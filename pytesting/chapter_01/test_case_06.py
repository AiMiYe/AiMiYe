import pytest

"""
测试类级别
    setup_class/teardown_class: 在测试类执行之前/之后执行
    setup_method/teardown_method: 在每一个测试方法执行之前/之后执行
    setup/teardown: 在每一个测试用例执行之前/之后执行
"""


class TestCaseDemo:
    def setup_class(self):
        print(f"==========setup_class==========")

    def teardown_class(self):
        print(f"========teardown_class=========")

    def setup_method(self):
        print(f"+++++++++setup_method+++++++++")

    def teardown_method(self):
        print(f"+++++++teardown_method++++++++")

    def setup(self):
        print(f"-----------setup------------")

    def teardown(self):
        print(f"----------teardown----------")

    def test_case_01(self):
        print("<-test_case_01->")
        assert 1 == 1

    def test_case_02(self):
        print("<-test_case_02->")
        assert 1 == 2


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case_06.py'])
