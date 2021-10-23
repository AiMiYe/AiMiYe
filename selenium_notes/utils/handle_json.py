import json
from selenium_notes.config import JSON


class HandleJSON:

    @staticmethod
    def load_json_file(file_name: str) -> dict:
        """
        读取json文件内容
        :param file_name: json文件路径
        :return:
        """
        return json.load(open(file_name, "r", encoding="UTF-8"))

    @staticmethod
    def write_json_file(file_name: str, content: str, append=False) -> None:
        """
        写入json文件
        :param file_name: json文件路径
        :param content: json文件内容
        :param append: 已追加的方式写入文件
        :return:
        """
        if append:
            with open(file_name, 'a', encoding="UTF-8") as fb:
                json.dump(content, fp=fb)
        with open(file_name, 'w', encoding="UTF-8") as fb:
            json.dump(content, fp=fb)


if __name__ == '__main__':
    print(HandleJSON.load_json_file(JSON))
