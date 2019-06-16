import sys

#
# Klasa: Token
# ------------
# przeztrzeń nazw dla konstant reprezentujacyh typy tokenów
#
class Token:
    NUMBER = "NUMBER"  # liczba
    VARIABLE = "VARIABLE"  # zmienna
    OPERATOR = "OPERATOR"  # operator
    LEFT_PARENTH = "("  # otwierający nawias
    RIGHT_PARENTH = ")"  # zamykający nawias
    HIGH_PRECEDENCE = 2  # wysoka priorytetność wykonania działania (zarezerwowane dla potęgowania)
    MIDDLE_PRECEDENCE = 1  # średnia priorytetność wykonania działania
    LOW_PRECEDENCE = 0  # niska priorytetność wykonania działania

#
# Funkcja: isoperator
# -------------------
# sprawdza czy argument jest operatorem
#     '*' => True
#
# argumenty:
#     1) c: <class 'str'> - ascii symbol
#
# zwraca:
#     <class 'bool'> - symbol był operatorem lub nie
#
def isoperator(c):
    return c in ('+', '-', '*', '/', '%')

#
# Funkcja: to_number
# ------------------
# konwertuje liste cyfer w liczbę
#     ['2, '3'] => 23
#
# argumenty:
#     1) buffer: <class 'list'> - lista z cyframi
#
# zwraca:
#     <class 'int'> | <class 'float'> - liczbe całkowitą lub zmiennopozycyjną zależnie od tego 
#     czy w liście była znaleziona kropka
#
def to_number(buffer):
    number = "".join(buffer)
    buffer.clear()
    
    if ('.' in number):
        return float(number)
    else:
        return int(number)

#
# Funkcja: new_token
# ------------------
# Fabrykuje słownik mieszczący dane o tokenie
#     (2, '/') => {"type": 2, "value": '/', "precedence": 2, "associativity": "left"}
#
# argumenty:
#     1) token_type: <class 'int'> - typ tokenu (z przeztrzeni nazw Token)
#     2) token_value: <class 'str'> - znaczenie tokenu
#
# zwraca:
#     <class 'dict'> - informacje o tokenie
#
def new_token(token_type, token_value):
    if token_type == Token.OPERATOR:
        if token_value in ('*', '/', '%'):
            precedence = Token.MIDDLE_PRECEDENCE
            associativity = 'left'
        elif token_value in ('+', '-'):
            precedence = Token.LOW_PRECEDENCE
            associativity = 'left'
        return {
            "type": token_type,
            "value": token_value,
            "precedence": precedence,
            "associativity": associativity  # dodana na przyszłośc, by można było dodać operator potęgowania
        }
    else:
        return {"type": token_type, "value": token_value}

#
# Funkcja: peek
# ------------
# funckcja pomocnicza przy pracy ze stosami - zwraca górni element ze stosu lub None, jeżeli stos jest pusty
# (nie usuwając jak standardowa funkcja pop)
#     [1, 2, 3, 4] => 4
#
# argumenty:
#     1) stack: <class 'int'> - stos
#
# zwraca:
#     <class 'int'> - górni (ostatni) element stosu
#
def peek(stack):
    return stack[-1] if stack else None

#
# Funkcja: greater_precedence
# --------------------
# wyznacza czy operator pierwszy ma pierwszenstwo nad operatorem drugim
#     ({'type': 2, 'value': '-', 'precedence': 3, 'associativity': 'left'},
#           {'type': 2, 'value': '*', 'precedence': 2, 'associativity': 'left'}) => False
#
# argumenty:
#     1) op1: <class 'dict'> - pierwszy operator
#     2) op2: <class 'dict'> - drugi operator
#
# zwraca:
#     <class 'bool'> True | False
#
def greater_precedence(op1, op2):
    return op1["precedence"] > op2["precedence"] 
    
#
# Funkcja: throw_error
# --------------------
# funkcja pomocnicza - wyrzuca pomyłkę i terminuje skrypt
#     "Internall error has occured" => (standardowe wyjście << "Error: Internal error has occured")
#
# argumenty:
#     1) message <class 'str'> - powiadomienie z pomyłką
#
# zwraca:
#     Jeżeli wszystko poszło dobrze funkcja nie zwraca kontrolu do wywołującej funkcji
#
def throw_error(message):
    print("Error:", message)
    sys.exit()
    
