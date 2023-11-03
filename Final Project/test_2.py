#!/usr/bin/env python3

import sys
from dagor import JuegoCaballosBailadores, JugadorCaballosBailadoresAleatorio, JugadorCaballosBailadoresInteractivo


if __name__ == '__main__':
    jugador1 = JugadorCaballosBailadoresInteractivo('Humano')
    jugador2 = JugadorCaballosBailadoresAleatorio('Maquina')

    juego = JuegoCaballosBailadores(jugador1, jugador2, 5, 6)
    juego.inicia()