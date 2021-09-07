import os
import sys
import configparser

sys.path.append(os.path.split(os.path.dirname(__file__))[0])

from selenium_notes.config import ELEMENT
from selenium_notes.utils.logUtils import logger


class HandleIni(object):
    def __init__(self, file: str):
        self.__config = configparser.ConfigParser()
        self.__config.read(file, encoding="UTF-8")

    def get_value(self, section: str, option: str, sep="-->"):
        """
        获取ini配置文件指定值
        :param section: 模块
        :param option: key
        :param sep: 值分隔符
        :return: 字符串类型值或者是元组类型值
        """
        value = "-1"
        try:
            result = self.__config.get(section, option)
            value = tuple(result.split(sep)) if sep in result else result
        except configparser.NoSectionError as _:
            logger.exception(f"No section: '{section}'")
        except configparser.NoOptionError as _:
            logger.exception(f"No option: '{option}'")
        return value

    def get_sections(self) -> list:
        """
        获取配置文件中所有的section
        :return:
        """
        return self.__config.sections()

    def get_option(self, section: str) -> list:
        """
        获取配置文件指定section的所有key
        :param section: 模块
        :return:
        """
        options = []
        try:
            options = self.__config.options(section)
        except configparser.NoSectionError as _:
            logger.exception(f"No section: '{section}'")
        return options

    def get_section_all_values(self, section: str) -> dict:
        """
        获取指定section下所有的key - value
        :param section:
        :return:
        """
        values = {}
        for i in self.get_option(section):
            rlt = self.get_value(section, i)
            values[i] = rlt
        return values


if __name__ == '__main__':
    ini = HandleIni(ELEMENT)
    print(ini.get_option('element'))
