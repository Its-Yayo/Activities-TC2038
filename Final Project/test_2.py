#!/usr/bin/env python3

import sys
from dagor import JuegoCaballosBailadores, JugadorCaballosBailadoresAleatorio, JugadorCaballosBailadoresInteractivo
from equipo14 import JugadorCaballosBailadoresEquipo14


if __name__ == '__main__':
    jugador1 = JugadorCaballosBailadoresEquipo14('Equipo14')
    jugador2 = JugadorCaballosBailadoresAleatorio('Random')
    jugador3 = JugadorCaballosBailadoresAleatorio('Random2')
    jugador4 = JugadorCaballosBailadoresInteractivo('Yo')
    jugador5 = JugadorCaballosBailadoresEquipo14('Equipo14')

    juego = JuegoCaballosBailadores(jugador1, jugador2, 6, 6)
    juego.inicia(veces=100, delta_max=2)
