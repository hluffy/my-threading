x = 1

def test():
    # 全局变量，要改变函数外的变量，必须用global修饰
    # global x
    x = 2
    print(x)


test()
print(x)