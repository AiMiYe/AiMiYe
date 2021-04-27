import os
from concurrent.futures import ThreadPoolExecutor


def main():
    with ThreadPoolExecutor(10) as thead:
        thead.map(lambda x: os.system(f"pip install -U {x}"),
                  [x.split("==")[0] for x in os.popen("pip freeze").readlines()])


if __name__ == '__main__':

    main()
