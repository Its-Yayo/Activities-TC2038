#!/usr/bin/env python3

import sys
from dagor import JuegoCaballosBailadores, JugadorCaballosBailadoresAleatorio, JugadorCaballosBailadoresInteractivo
from equipo14 import JugadorCaballosBailadoresEquipo14
from equipo14test import JugadorTest


if __name__ == '__main__':
    jugador1 = JugadorCaballosBailadoresEquipo14('Equipo14')
    jugador2 = JugadorCaballosBailadoresAleatorio('Random')
    jugador3 = JugadorCaballosBailadoresAleatorio('Random2')
    jugador4 = JugadorCaballosBailadoresInteractivo('Yo')
    jugador5 = JugadorTest('Equipo14 Test')

    juego = JuegoCaballosBailadores(jugador2, jugador5, 5, 5)
    juego.inicia(delta_max=2, veces=100)
