import re

"""
    <instruction> ::= <affectation> | <conditionnelle>
    <conditionnelle> ::= ? <condition> : <affectation>
    <condition> ::= <expression> {=|#} <expression>
    <affectation> ::= <identificateur> = <expression>
    <expression> ::= <facteur> {+|-} <expression> | <facteur>
    <facteur> ::= <terme> {*|/} <facteur> | <terme>
    <terme> ::= <identificateur> | <nombre> | ( <expression> )
"""


class Parseur:

    listeLexicale = ['[a-zA-Z0-9]', '[-]', '[+]', '[?]', '[:]', '[#]', '[=]', '[*]', '[/]', '\s']

    tabExpression = []

    def __init__(self):
        self.remplir()

    def analyse(self):
        for index, valeur in enumerate(self.tabExpression):
            for value in valeur:
                error = 1
                for regex in self.listeLexicale:
                    if re.search(regex, value):
                        error = 0
                if error == 1:
                    print('Erreur !\nAt line ' + str(index + 1) + '\n' + value + ' sur l\'expression ' + valeur)
                    print('')
                    break


    def afficherTab(self):
        for compteur, i in enumerate(self.tabExpression):
            print('['+str(compteur+1)+']: ' + i)


    def remplir(self):
        valeur = input(' =>Veuillez entrer une expression (Ou rien pour finir): \n')
        if (valeur == ''):
            return
        self.tabExpression.append(valeur)
        return self.remplir()


parse = Parseur()
parse.afficherTab()
print('\n')
parse.analyse()