"""result.py - Se confirma si el jugador ganó o perdió el juego."""

from development.state import show_state

def show_result():
    if show_state() > 0:
        return '¡Ganaste!'
    else:
        return 'Perdiste :('