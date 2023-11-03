#!/usr/bin/env python3

import sys
from dagor import JuegoD10, JugadorD10Interactivo, JugadorD10Estrategico


def main() -> None:
    jugador1 = JugadorD10Estrategico('Maquina')
    jugador2 = JugadorD10Interactivo('Me')

    juego = JuegoD10(jugador1, jugador2)
    juego.inicia()


if __name__ == '__main__':
    main()
    sys.exit(1)