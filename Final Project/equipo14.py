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

class JugadorCaballosBailadoresEquipo14(JugadorCaballosBailadores):
    ''' The basis of our strat is that basically, our knight will always look for the center of the board
    in order to make the best position, using an adversarial search algorithm like Minimax. It maybe can kill
    the other's knight or king.When it finds a good position, the knight will follow a path in other to win.
    Code will be documented. '''

    # Heuristica method. My knight will always try to dominate the center in order to check the best move
    def heuristica(self, posicion):
        # Positions around the puzzle
        turno, _, _, _, _, cN, cB = posicion
        my_knight = cB if self.simbolo == 'B' else cN
        opponent_king = cN if self.simbolo == 'B' else cB
        opponent_knight = cB if self.simbolo == 'N' else cN

        # Manhattan distance for either my knight and the other's king and knight
        distance_king = abs(my_knight[0] - opponent_king[0]) + abs(my_knight[1] - opponent_king[1])
        distance_knight = abs(my_knight[0] - opponent_knight[0]) + abs(my_knight[1] - opponent_knight[1])

        # Check if my knight is in danger of the other's knight
        danger = 1 if distance_knight == 2.5 else 0

        # My knight will dominate the center. It uses the Manhattan distance as well
        max_m = max(my_knight[0], opponent_king[0], opponent_knight[0])
        max_n = max(my_knight[1], opponent_king[1], opponent_knight[1])
        center = (max_m / 2, max_n / 2)
        distance_center = abs(my_knight[0] - center[0]) + abs(my_knight[1]) - abs(center[1])

        # Constant to check if the distance king is zero. It raises an exception when my knight and the other's king are in the same position
        value = 100 / (distance_king + 1e-6) * 2.5- distance_knight * 2.5 - distance_center - danger * 50

        return value


    # Tira method. It uses Minimax with the alpha-beta prunning in order to make the best moves according to the heuristica method
    # It uses a default 3 or 4 depth. It has no more cuz of a runtime exception of 2 sec
    def tira(self, posicion):
        # Depth for an adversarial search
        max_depth = 4

        # Nested function that prioritizes movements
        def prioritize_movement(movement):
            return sorted(movement, key=lambda m: self.heuristica(m), reverse=True)


        # I forgot, it uses recursion too lol
        def minimax(posicion, depth, alpha, beta, max_player):
            if depth == 0 or self.triunfo(posicion) is not None:
                return self.heuristica(posicion), posicion

            if max_player:
                max_eval = float('-inf')
                best = None

                for child in prioritize_movement(self.posiciones_siguientes(posicion)):
                    eval, _ = minimax(child, depth - 1, alpha, beta, False)

                    if eval > max_eval:
                        max_eval = eval
                        best = child

                    alpha = max(alpha, eval)

                    if beta <= alpha:
                        break

                return max_eval, best
            else:
                min_eval = float('inf')
                best = None

                for child in prioritize_movement(self.posiciones_siguientes(posicion)):
                    eval, _ = minimax(child, depth - 1, alpha, beta, True)

                    if eval < min_eval:
                        min_eval = eval
                        best = child

                    beta = min(beta, eval)

                    if beta <= alpha:
                        break

                return min_eval, best

        _, best = minimax(posicion, max_depth, float('-inf'), float('inf'), True)

        return best
