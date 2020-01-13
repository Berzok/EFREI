#coding: utf-8


def facto(x):
    if x == 1:
        return x
    return x*facto(x-1)

def expo(x):
    result = float(1+x)
    print(result)
    for i in range(2, 40):
        result += (x**i)/facto(i)
    return result


x = float(input())

print(expo(x))