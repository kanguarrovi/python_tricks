
def func1():
    pass


def func2():
    pass


def func3():
    pass


#  For functions. Instead doing this.

number = int(input())

if number == 1:
    func1()
elif number == 2:
    func2()
else:
    func3()


# Do this

number = int(input())

func_map = {
    1: func1,
    2: func2
}

func_map.get(number, func3)
