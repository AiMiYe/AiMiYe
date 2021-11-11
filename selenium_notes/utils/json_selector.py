import os
import sys
import json
from jsonpath import jsonpath

sys.path.append(os.path.split(os.path.dirname(__file__))[0])


class JSONSelector(object):
    """
    json格式数据提取器
    """

    def __init__(self, string: str):
        self.__json_ojb = json.loads(string)

    def get_value(self, json_path: str):
        """
        获取指定的值
        :param json_path:
        :return:
        """
        value = "-1"
        if json_path.startswith("$."):
            index = json_path[2]
            if index != ".":
                rlt = jsonpath(self.__json_ojb, json_path)
                if isinstance(rlt, list):
                    value = rlt[0]
            else:
                rlt = jsonpath(self.__json_ojb, json_path)
                if isinstance(rlt, list):
                    value = rlt
        return value


if __name__ == '__main__':
    txt = """1111"""
    js = JSONSelector(txt)
    print(js.get_value("$.success"))
