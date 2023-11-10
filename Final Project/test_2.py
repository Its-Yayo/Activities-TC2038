#!/usr/bin/env python3

import sys
from dagor import JuegoCaballosBailadores, JugadorCaballosBailadoresAleatorio, JugadorCaballosBailadoresInteractivo
from equipo14 import JugadorCaballosBailadoresEquipo14


if __name__ == '__main__':
    jugador1 = JugadorCaballosBailadoresEquipo14('Equipo14')
    jugador2 = JugadorCaballosBailadoresAleatorio('Random')

    juego = JuegoCaballosBailadores(jugador2, jugador1, 7, 7)
    juego.inicia(veces=100, delta_max=2)
