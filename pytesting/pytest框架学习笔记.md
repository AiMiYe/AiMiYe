# Pytest自动化测试框架

## 1. 安装pytest

```bash
pip install pytest -U
```

## 2. 验证pytest框架安装成功

```bash
pytest --vetsion
```

## 3. pytest中文官方文档

中文官方文档： https://www.osgeo.cn/pytest/contents.html

## 4. pytest加载执行测试用例规则

1. 将当前目录及其子目录中运行所有文件名以`test_*.py`或`*_test.py`的文件
2. 以`test_*`开头的函数
3. 以`Test*`开头的类，`test_*`开头的方法，并且不能带有`__init__ `方法
4. 所有的包pakege必须要有`__init__.py`文件

