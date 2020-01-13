# coding: utf-8

def makeListe(entree):
    liste = []
    test = 0

    for index, valeur in enumerate(entree):

        if valeur == '+' or valeur == '-' or valeur == '*' or valeur == '/' or valeur == '(' or valeur == ')':
            if entree[test:index] != '':
                liste.append(entree[test:index])
            liste.append(valeur)
            test = index + 1

    liste.append(entree[test:])

    return liste


def calculate(liste):
    for index, valeur in enumerate(liste):
        if valeur == '*':
            liste[index] = float(liste[index - 1]) * float(liste[index + 1])
            liste.pop(index + 1)
            liste.pop(index - 1)

        if valeur == '/':
            liste[index] = float(liste[index - 1]) / float(liste[index + 1])
            liste.pop(index + 1)
            liste.pop(index - 1)
        print(liste)

    for index, valeur in enumerate(liste):
        if valeur == '+':
            liste[index] = float(liste[index - 1]) + float(liste[index + 1])
            liste.pop(index + 1)
            liste.pop(index - 1)
        if valeur == '-':
            liste[index] = float(liste[index - 1]) - float(liste[index + 1])
            liste.pop(index + 1)
            liste.pop(index - 1)

    if len(liste) > 1:
        return calculate(liste)

    return liste[0]


def calcul(liste):
    for index, valeur in enumerate(liste):
        if valeur == '(':
            return calcul(liste[index + 1:])

        if valeur == ')':
            return calculate(liste[:index])


def regroupement(liste):
    while '(' in liste:
        remplacement = calcul(liste)
        number = 0
        for index, valeur in enumerate(liste):
            if valeur == '(':
                number = index
            if valeur == ')':
                for i in range(index - number):
                    liste.pop(number)

                print(liste)
                liste[number] = remplacement
                print(liste)

    return calculate(liste)


entree = '52+5+3/6+(2/(1+4*2))*6'
print(makeListe(entree))
print(regroupement(makeListe(entree)))
