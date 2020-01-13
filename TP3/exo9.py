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

    types = ['instruction', 'conditionnelle', 'condition', 'affectation', 'expression', 'facteur', 'terme']

    identificateur = '\b\w{1}\d*\b'
    nombre = '\b\d+'



    def __init__(self, expression):
        self.expression = expression

    def analyser(self):
        pass

    def findType(self, expression):


expression = 'A1 = A * 100 + 2*B'
expression2 = '? A1 = B : C = D'