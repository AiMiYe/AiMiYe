import os
import sys
import string
import random
import operator
from functools import reduce

sys.path.append(os.path.split(os.path.dirname(__file__))[0])


def generate_letter(digit: int, sep="") -> str:
    """
    生成随机大小写字母字符串
    :param digit: 字符串位数
    :param sep: 字符串分隔符
    :return:
    """
    return f"{sep}".join(random.sample(string.ascii_letters, digit))


def generate_letter_and_number(digit: int, sep="") -> str:
    """
    生成随机大小写字母，数字字符串
    :param digit: 字符串位数
    :param sep: 字符串分隔符
    :return:
    """
    return f"{sep}".join(random.sample(string.ascii_letters + string.digits, digit))


def generate_chinese(digit: int, sep="") -> str:
    """
    生成随机中文字符串
    :param digit: 字符串位数
    :param sep: 字符串分隔符
    :return:
    """
    return f"{sep}".join([chr(random.randint(0, 27605) + 13312) for _ in range(digit)])


def generate_number(digit: int, sep="") -> str:
    """
    生成随机数字字符串
    :param digit: 字符串位数
    :param sep: 字符串分隔符
    :return:
    """
    return f"{sep}".join([string.digits[random.randint(0, 9)] for _ in range(digit)])


def generate_phone() -> str:
    """
    随机生成手机号码
    :return:
    """
    prefix = (
        "133", "149", "153", "173", "177", "180", "181", "189", "199", "130", "131", "132", "145", "155", "156", "166",
        "171", "175", "176", "185", "186", "166", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
        "157", "158", "159", "172", "178", "182", "183", "184", "187", "188", "198")
    return prefix[random.randint(0, len(prefix) - 1)] + generate_number(8)


def conversion_to_elevate(array: list, size: int) -> list:
    """
    一维列表转二维列表
    :param array: 原始列表
    :param size: 二维列表中元素列表长度
    :return: 二维列表
    """
    return [array[i:i + size] for i in range(0, len(array), size)]


def conversion_to_reduce(array: list) -> list:
    """
    二维数组转一维数组
    :param array: 二维数组
    :return: 一维数组
    """
    return reduce(operator.add, array)


if __name__ == '__main__':
    print(generate_chinese(2))
