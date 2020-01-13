# coding: utf-8

def makeListe(entree):
    liste = []
    compteur = 0
    for index, valeur in enumerate(entree):
        if valeur == '+' or valeur == '-' or valeur == '*' or valeur == '/' or valeur == '(' or valeur == ')':
            if entree[compteur:index] != '':
                liste.append(entree[compteur:index])
            liste.append(valeur)
            compteur = index + 1
    liste.append(entree[compteur:])
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


def prepareCalcul(liste):
    for index, valeur in enumerate(liste):
        if valeur == '(':
            return prepareCalcul(liste[index + 1:])
        if valeur == ')':
            return calculate(liste[:index])


def diminution(liste):
    while '(' in liste:
        remplacement = prepareCalcul(liste)
        number = 0
        for index, valeur in enumerate(liste):
            if valeur == '(':
                number = index
            if valeur == ')':
                for i in range(index - number):
                    liste.pop(number)
                liste[number] = remplacement
    return calculate(liste)


def verifInput(liste):
    nbParentheseOuvrantes = 0
    nbParentheseFermantes = 0
    print(liste)
    for index, valeur in enumerate(liste):
        if not valeur.isdigit() and valeur not in ['+', '-', '*', '/', '(', ')', '.']:
            return 0
        if valeur == '(':
            nbParentheseOuvrantes += 1
        if valeur == ')':
            nbParentheseFermantes += 1
        if valeur == '+' or valeur == '-' or valeur == '/' or valeur == '*':
            if liste[index + 1] == '+' or liste[index + 1] == '-' or liste[index + 1] == '/' or liste[index + 1] == '*':
                return 0
    if nbParentheseFermantes != nbParentheseOuvrantes:
        return 0
    return 1


entree = str(input())
while verifInput(entree) == 0:
    print('pas bon')
    entree = str(input())
entree = makeListe(entree)
print(entree)
print(diminution(entree))
