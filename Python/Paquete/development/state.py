"""state.py - Se muestra el total de los puntos obtenidos."""

from development.points import validation

def show_state():
    print('El total de los puntos obtenidos es:', validation())
    return validation()
