def decorator(func):
    def count(a, b):
        print(f"函数名称： {add.__name__}")
        func(a, b)

    return count


@decorator
def add(a, b):
    print(f"函数名称： {add.__name__}")
    print(f"{a + b}")


if __name__ == '__main__':
    add(1,2)
