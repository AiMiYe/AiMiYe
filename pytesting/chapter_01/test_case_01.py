import pytest

"""
1. 安装pytest
    pip install pytest -U
2. 验证pytest框架安装成功
    pytest --vetsion
3. pytest中文官方文档
    中文官方文档： https://www.osgeo.cn/pytest/contents.html
4. pytest加载执行测试用例规则
    1. 将当前目录及其子目录中运行所有文件名以`test_*.py`或`*_test.py`的文件
    2. 以`test_*`开头的函数
    3. 以`Test*`开头的类，`test_*`开头的方法，并且不能带有`__init__ `方法
    4. 所有的包package必须要有`__init__.py`文件
5. pytest.ini配置文件参数说明：
    testpaths: 用于指定测试用例加载目录
6. pytest生成测试报告
    1. 生成xml测试报告
        pytest test_case_03.py -s -v --junit-xml=./report/rlt.xml
    2. 生成在线测试报告
        pytest test_case_03.py -s -v --pastebin=all
7. pytest 命令行选项
    1. pytest --fixtures 查看pytest内置函数命令
    2. --maxfail=2 设置用例最大失败次数
8. 多线程执行测试用例
    1. 安装插件pytest-xdist
        pip install pytest-xdist
    2. 多线程执行测试用例命令(-n 线程数/auto)
        pytest test_case_03.py -s -v -n 3
9. pytest失败用例重跑
    1. 安装插件pytest-rerunfailures
        pip install pytest-rerunfailures
    2. 失败用例重跑命令行参数(--reruns 最大重跑次数)
        pytest test_case_01.py -s --reruns 5
    3. 失败用例重跑睡眠时间命令行参数(--reruns-delay 秒数)
        pytest test_case_01.py -s --reruns 5 --reruns-delay 5
10. 获取用例执行性能数据
    1. 获取执行最慢的测试用例( --durations=5/用例个数)
    
"""


@pytest.mark.slow
def test_case_01():
    print("test_case_01 目录下的测试用例")
    assert ord('A') == 65


def test_case_02():
    print("test_case_02 目录下的测试用例")
    assert ord('A') != 65


if __name__ == '__main__':
    # pytest.main(['-s', 'test_case_01.py', '-m', 'slow'])
    pytest.main(['-s', 'test_case_01.py', '--reruns', '3'])
