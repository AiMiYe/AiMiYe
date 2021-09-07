import json
from selenium_notes.config import JSON


def load_json_file(file_name: str) -> dict:
    """
    读取加载json文件
    :param file_name: json文件路径
    :return:
    """
    return json.load(open(file_name, "r", encoding="UTF-8"))


def write_json_file(file_name: str) -> dict:
    pass


if __name__ == '__main__':
    print(load_json_file(JSON))
