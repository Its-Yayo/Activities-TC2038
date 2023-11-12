#!/usr/bin/python3.12

# test code purposes

from dagor import *

class JugadorTest(JugadorCaballosBailadores):
    def heuristica(self, posicion):
        turno, _, _, _, _, cN, cB = posicion
        my_knight = cB if self.simbolo == 'B' else cN
        opponent_king = cN if self.simbolo == 'B' else cB
        opponent_knight = cB if self.simbolo == 'N' else cN

        # Manhattan distance for either my knight and the other's king and knight
        distance_king = abs(my_knight[0] - opponent_king[0]) + abs(my_knight[1] - opponent_king[1])
        distance_knight = abs(my_knight[0] - opponent_knight[0]) + abs(my_knight[1] - opponent_knight[1])

        # Constant to check if the distance king is zero. It raises an exception when my knight and the other's king are in the same position
        value = 100 / (distance_king + 1e-6) - distance_knight

        return value

    def tira(self, posicion):

        # Depth for an adversarial search
        max_depth = 4
        def minimax(posicion, depth, alpha, beta, max_player):
            if depth == 0 or self.triunfo(posicion) is not None:
                return self.heuristica(posicion), posicion

            if max_player:
                max_eval = float('-inf')
                best = None

                for child in self.posiciones_siguientes(posicion):
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

                for child in self.posiciones_siguientes(posicion):
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
