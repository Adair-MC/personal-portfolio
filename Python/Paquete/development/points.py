"""points.py - En base al resultado de la comparación, se suman o restan puntos."""

from development.bet import bet_init

res = bet_init()

def validation():
    wallet = 0
    if res == True:
        wallet += 1
        return wallet
    if res == False:
        wallet -= 1
        return wallet