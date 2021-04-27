# python 反射
"""
class Demo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print(f"调用 work 成功!")

    def add(self, x, y):
        print(x + y)


if __name__ == '__main__':
    demo = Demo('look', 30)
    demo.work()
    demo.add(2, 2)

    # 通过反射获取属性
    print(getattr(demo, 'name'))
    print(getattr(demo, 'age'))
    # 通过反射调用方法
    getattr(demo, 'work')()
    getattr(demo, 'add')(2, 3)
    # 通过反射设置属性
    setattr(demo, 'name', 'like')
    setattr(demo, 'age', 25)
    print(getattr(demo, 'name'))
    print(getattr(demo, 'age'))
    # 通过反射判断对象是否包含指定属性
    print(hasattr(demo, "name"))
    print(hasattr(demo, "work"))
    print(hasattr(demo, "like"))
    print(callable(demo))
"""
