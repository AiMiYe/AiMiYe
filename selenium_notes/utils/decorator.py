import os
import sys

sys.path.append(os.path.split(os.path.dirname(__file__))[0])


def timers(timer=1):
    def decorator(func):
        def count(a, b, *args, **kwargs):
            print(f"函数名称： {add.__name__}")
            for i in range(timer):
                rlt = func(a, b, *args, **kwargs)
            return rlt

        return count

    return decorator


@timers(5)
def add(a, b, *args, **kwargs):
    return a + b + sum(args)


if __name__ == '__main__':
    print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))
