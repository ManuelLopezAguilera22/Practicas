from piedra_papel_tijeras import *
def jugar():
    ''' 
    Ejecuta una partida al mejor de 3 rondas del juego piedra, papel o tijeras. 
    '''
    print("🎮 ¡Bienvenido al juego Piedra, Papel o Tijeras! Vamos al mejor de 3 rondas.")

    usuario_decide_jugada, determinar_ganador = declarar_funciones()

    puntuacion_usuario = 0
    puntuacion_ordenador = 0
    ronda = 1

    while puntuacion_usuario < 2 and puntuacion_ordenador < 2:
        print(f"\n🔁 Ronda {ronda}")
        opciones = ["piedra", "papel", "tijeras"]
        jugada_ordenador = random.choice(opciones)
        jugada_usuario = usuario_decide_jugada()

        print(f"🖥️ El ordenador ha elegido: {jugada_ordenador}")

        resultado = determinar_ganador(jugada_usuario, jugada_ordenador)

        if resultado == "empate":
            print("🤝 ¡Es un empate!")
        elif resultado == "usuario":
            puntuacion_usuario += 1
            print("✅ ¡Has ganado esta ronda!")
        else:
            puntuacion_ordenador += 1
            print("❌ ¡Ha ganado el ordenador esta ronda!")

        print(f"📊 Marcador: Tú {puntuacion_usuario} - Ordenador {puntuacion_ordenador}")
        ronda += 1

    if puntuacion_usuario == 2:
        print("\n🏆 ¡Felicidades! Has ganado la partida al mejor de 3.")
    else:
        print("\n💻 El ordenador ha ganado la partida. ¡Suerte para la próxima!")

if __name__ == "__main__":
    jugar()
