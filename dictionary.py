
def ex1(num):
    try:
        return 6 / num
    except ZeroDivisionError:
        return -1


def ex2(index, my_tuple=(1,2,3,4,5)):
    try:
        return my_tuple[index]
    except IndexError:
        return -9
    except NameError:
         return -2



def ex3(name):
    try:
        return "hello" + name
    except NameError:
        return -9


if __name__ == '__main__':
    # Run your functions here
    print(ex3(""))
    print(ex2(5))
    print(ex1(0))
    print("Good Luck!")
