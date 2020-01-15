#coding: utf-8
import math

def facto(x):
    if x == 1:
        return x
    return x*facto(x-1)

def expo(x, iter):
    result = float(1+x)
    for i in range(2, iter):
        result += (x**i)/facto(i)
    return result


x = float(input('Choisissez votre nombre: '))
iter = int(input("Nombre d'itérations: "))

print(expo(x, iter))