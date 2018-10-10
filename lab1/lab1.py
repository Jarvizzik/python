def  func1(num1,num2):

    bool = True
    if (num1 < 0 or num2 < 0):
        raise Exception('Number must be positive')
    if (num1 % num2 != 0):
        bool = False
    return bool

def func2(s, e):
    arr = []
    if (s < 0 or e < 0):
        raise Exception('Number must be positive')
    for i in range(s, e+1):
        test=True
        for j in range(2, i):
            if (func1(i, j)):
                test=False
        if(test):
            arr.append(i)

    if len(arr) == 0:
        raise Exception('NoSimpleDigits')
    return arr


arr2=['a', ['c', 1, 3], ['f', 7, [4, ['4']]], [{'lalala': 111}]]
arr3 = []
def func3(l):
    for i in range(0, len(l)):
        if(isinstance(l[i], list)):
            func3(l[i])
        else:
            arr3.append(l[i])
    return arr3

