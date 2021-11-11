import os


def find_file(directory, key_words):
    """
    在指定目录中查询文件
    :param directory: 目标目录
    :param key_words: 查找关键字
    :return: None
    """
    for i in os.listdir(directory):
        path = os.path.join(directory, i)
        if key_words in i:
            print(path)
        if os.path.isdir(path):
            find_file(path, key_words)


if __name__ == '__main__':
    find_file(r'D:\maven', 'jedis')
