# def pytest_collection_modifyitems(items):
#     """
#     通过钩子函数重新编码测试用例中使用的中文描述字符
#     :param items:
#     :return:
#     """
#     for item in items:
#         item.name = item.name.encode('UTF-8').decode("unicode_escape")
#         item._nodeid = item.nodeid.encode('UTF-8').decode("unicode_escape")
