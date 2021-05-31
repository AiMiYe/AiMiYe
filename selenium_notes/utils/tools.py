import string
import random


def generate_letter(digit, sep=""):
    """
    生成随机大小写字母字符串
    :param digit: 字符串位数
    :param sep: 字符串分隔符
    :return:
    """
    return f"{sep}".join(random.sample(string.ascii_letters, digit))


def generate_letter_and_number(digit, sep=""):
    """
    生成随机大小写字母，数字字符串
    :param digit: 字符串位数
    :param sep: 字符串分隔符
    :return:
    """
    return f"{sep}".join(random.sample(string.ascii_letters + string.digits, digit))


def generate_chinese(digit, sep=""):
    """
    生成随机中文字符串
    :param digit: 字符串位数
    :param sep: 字符串分隔符
    :return:
    """
    return f"{sep}".join([chr(random.randint(0, 27605) + 13312) for _ in range(digit)])


def generate_number(digit, sep=""):
    """
    生成随机数字字符串
    :param digit: 字符串位数
    :param sep: 字符串分隔符
    :return:
    """
    return f"{sep}".join([string.digits[random.randint(0, 9)] for _ in range(digit)])


def generate_phone():
    """
    随机生成手机号码
    :return:
    """
    prefix = (
        "133", "149", "153", "173", "177", "180", "181", "189", "199", "130", "131", "132", "145", "155", "156", "166",
        "171", "175", "176", "185", "186", "166", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
        "157", "158", "159", "172", "178", "182", "183", "184", "187", "188", "198")
    return prefix[random.randint(0, len(prefix) - 1)] + generate_number(8)


if __name__ == '__main__':
    print(generate_chinese(2, ""))
    print(generate_number(18, ""))
    print(generate_letter(10))
    print(generate_letter_and_number(12))
    print(generate_phone())
