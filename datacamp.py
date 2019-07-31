def func1():
    num = 3
    print(num)

def func2():
    global num
    num = 6
    double_num = num * 2
    print(double_num)

func1()
func2()
print(num)