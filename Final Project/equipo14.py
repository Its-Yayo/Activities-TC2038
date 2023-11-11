#!/usr/bin/python3.12

# Project: Knight’s Dance
# Our new player is coming upppppppp
#
# @date: 29-Nov-2023
# @authors:
#           A01754574 Luis Fernando De León Silva
#           A01746999 Luis Eduardo Landeros Hernandez
#
# Repo: https://github.com/Its-Yayo/Activities-TC2038
# Code under free license.
# ----------------------------------------------------------

from dagor import *
from random import random

class JugadorCaballosBailadoresEquipo14(JugadorCaballosBailadores):
    ''' Our player is rising upppp.

    Basically, our strat follows this: The knight automatically
    follows a path in other to kill the king. Because of that,
    the knight will be guided by a generated tree until a certain tree
    in order to check a possible place where the knight fits in. The
    Minimax Algorithm is going to choose what's the best position for the knight.
    It also uses Minimax since our player is assuming the other's knight has an strat
    too. '''

    def heuristica(self, posicion):
        '''
        turno, _, _, rB, rN, cN, cB = posicion
        opponent_king = rN if turno == 'B' else rB
        opponent_knight = cN if turno == 'B' else cB
        mine = cN if turno == 'N' else cB

        # Manhattan Distance for either the other's king or knight.
        # If there's a place where the other's knight can kill mine's, it penalizes the move
        distance_king = abs(mine[0] - opponent_king[0]) + abs(mine[1] - opponent_king[1])
        distance_knight = abs(mine[0] - opponent_knight[0]) + abs(mine[1] - opponent_knight[1])

        movements = len(self.posiciones_siguientes(posicion))
        value = 5 * movements - 3 * distance_king - 2 * distance_knight

        return value '''

        # Testing a controlled random choice
        return random()

    def tira(self, posicion):
        # turno, _, _, _, _, cN, cB = posicion

         # It uses a tree to look out for a shot
        tree = self.arbol(posicion, 4)
        _, movement = self.minimax(tree, True)

        return movement


    # Additional function that generates a tree in order to check all the possible movements
    def arbol(self, posicion, depth):
        if depth == 0 and self.juego.juego_terminado(posicion):
            return (self.heuristica(posicion), None)

        movements = self.posiciones_siguientes(posicion)
        tree = []

        for movement in movements:
            tree.append((self.heuristica(movement), movement))

        return tree


    # Minimax algorithm to make the best move
    def minimax(self, tree, max):
        if len(tree) == 1:
            return tree[0]

        if max:
            max_value = float('-inf')
            max_movement = None

            for value, movement in tree:
                if value > max_value:
                    max_value = value

                max_movement = movement

            return max_value, max_movement
        else:
            min_value = float('inf')
            min_movement = None

            for value, movement in tree:
                if value > min_value:
                    min_value = value

                min_movement = movement

            return min_value, min_movement

