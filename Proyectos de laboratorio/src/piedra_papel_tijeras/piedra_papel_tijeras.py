import random

def declarar_funciones():
    def usuario_decide_jugada():
        ''' 
        Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
        '''
        eleccion_usuario = input("Elige piedra, papel o tijeras: ")
        while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
            eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")
        return eleccion_usuario

    def determinar_ganador(jugada_usuario, jugada_ordenador):
        ''' 
        Determina el ganador según las reglas del juego. 
        Devuelve "usuario", "ordenador" o "empate".
        '''
        if jugada_usuario == jugada_ordenador:
            return "empate"
        elif (jugada_usuario == "piedra" and jugada_ordenador == "tijeras") or \
             (jugada_usuario == "papel" and jugada_ordenador == "piedra") or \
             (jugada_usuario == "tijeras" and jugada_ordenador == "papel"):
            return "usuario"
        else:
            return "ordenador"

    return usuario_decide_jugada, determinar_ganador