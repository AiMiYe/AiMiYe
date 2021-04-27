import os
from concurrent.futures import ThreadPoolExecutor

try:
    from you_get.version import script_name
except ModuleNotFoundError as e:
    os.system("pip install you-get -i https://pypi.doubanio.com/simple")


def down_video(url):
    """[summary]

    Args:
        url ([type]): [description]
    """
    print(url)
    os.system(f"you-get -o G:\\video {url}")


def start(dir, BV, number):
    if not os.path.exists(dir):
        os.mkdir(dir)

    urls = (f"https://www.bilibili.com/video/{BV}?p={i}" for i in range(187, number + 1))
    with ThreadPoolExecutor(max_workers=30 if number > 20 else number) as thread:
        thread.map(down_video, urls)


def main():
    dir_path = r"G:\video"
    bv = "BV1PJ411n7xZ"
    number = 381

    for _ in range(1):
        start(dir_path, bv, number)

    print("删除无效弹幕文件...")
    for i in os.listdir(dir_path):
        if i.endswith(".cmt.xml"):
            os.remove(os.path.join(dir_path, i))


if __name__ == '__main__':
    main()
