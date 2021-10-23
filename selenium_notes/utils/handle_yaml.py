import yaml
from selenium_notes.config import YAML
from selenium_notes.config import JSON
from selenium_notes.utils.handle_json import HandleJSON


class HandleYAML:
    @staticmethod
    def load_yaml_file(file_name: str) -> dict:
        """
        读取加载yaml文件
        :param file_name: yaml文件路径
        :return:
        """
        with open(file_name, "r", encoding='UTF-8') as f:
            result = yaml.safe_load(f)
        return result

    @staticmethod
    def write_yaml_file(file_name: str, content: str, append=False) -> None:
        """
        写入yaml文件
        :param file_name: yaml文件路径
        :param content: yaml文件内容
        :param append: 已追加的方式写入文件
        :return:
        """
        if append:
            with open(file_name, 'a', encoding="UTF-8") as fb:
                yaml.safe_dump(content, fb)
        with open(file_name, 'w', encoding="UTF-8") as fb:
            yaml.safe_dump(content, fb)


if __name__ == '__main__':
    con = HandleJSON.load_json_file(JSON)
    # HandleYAML.write_yaml_file(YAML, con)
    print(HandleYAML.load_yaml_file(YAML))
