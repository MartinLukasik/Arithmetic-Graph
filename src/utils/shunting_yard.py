from utils.utils import *

#
# Funkcja: convert
# ----------------
# tłumaczy notację infiksową na ODP (https://pl.wikipedia.org/wiki/Odwrotna_notacja_polska)
#    [2, '-', 2] => [2, 2, '-']
#
# argumenty:
#    1) tokens: <class 'list'> - lista tokenów w notacji infiksowej
#
# zwraca:
#    <class 'list'> - lista tokenów w notacji posfiksowej
#
def convert(tokens):
    outq, stack = [], []

    for token in tokens:
        if token["type"] is Token.NUMBER or token["type"] is Token.VARIABLE:
            outq.append(token)
        elif token["type"] is Token.LEFT_PARENTH:
            stack.append(token)
        elif token["type"] is Token.RIGHT_PARENTH:
            top = peek(stack)
            while top is not None and top["type"] is not Token.LEFT_PARENTH:
                outq.append(stack.pop())
                top = peek(stack)
            stack.pop()
        else:
            top = peek(stack)
            while top is not None and top["type"] not in "()" and greater_precedence(top, token):
                outq.append(stack.pop())
                top = peek(stack)
            stack.append(token)
    outq.extend(stack[::-1]) 

    return outq
