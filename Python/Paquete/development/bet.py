"""bet.py - Donde el usuario hace una apuesta y se devuelve en razón de una comparación."""
import random

def bet_init():
    user_input = int(input('Ingrese un número del 1 al 20.\n >> '))
    random_n = random.randint(1, 20)
    print('El número generado aleatoriamente fue:', random_n)
    if user_input == random_n:
        print('¡Atinaste!')
        return True
    elif user_input < 0 or user_input > 20:
        print('⛔ Número inválido, por ende, pierdes punto. ⛔')
        return False
    else:
        print('¡No atinaste!')
        return False