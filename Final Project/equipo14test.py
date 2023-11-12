#!/usr/bin/python3.12

# test code purposes

from dagor import *

class JugadorTest(JugadorCaballosBailadores):
    def heuristica(self, posicion):
        turno, _, _, _, _, cN, cB = posicion
        my_knight = cB if self.simbolo == 'B' else cN
        opponent_king = cN if self.simbolo == 'B' else cB
        opponent_knight = cB if self.simbolo == 'N' else cN

        # Manhattan Distance for either my knight and the other's king and knight
        distance_king = abs(my_knight[0] - opponent_king[0]) + abs(my_knight[1] - opponent_king[1])
        distance_knight = abs(my_knight[0] - opponent_knight[0]) + abs(my_knight[1] - opponent_knight[1])

        value = 100 / (distance_king + 1e-6) - distance_knight

        return value

    def tira(self, posicion):
        '''
        turno, _, _, _, _, cN, cB = posicion

        # Define a helper function to check if the move is valid
        def is_valid_move(coord1, coord2):
            return (
                    abs(coord1[0] - coord2[0]) == 2 and abs(coord1[1] - coord2[1]) == 1
                    or abs(coord1[0] - coord2[0]) == 1 and abs(coord1[1] - coord2[1]) == 2
            )

        # Check if the opponent's knight can be captured in the next move
        opponent_knight = cN if turno == 'B' else cB
        if self.simbolo == 'B' and is_valid_move(cB, opponent_knight):
            return self.posiciones_siguientes(posicion)[0]

        if self.simbolo == 'N' and is_valid_move(cN, opponent_knight):
            return self.posiciones_siguientes(posicion)[0]

        valid_moves = self.posiciones_siguientes(posicion)
        if valid_moves:
            return valid_moves[0]

        return None '''

        max_depth = 3

        def minimax(posicion, depth, max_player):
            if depth == 0 or self.triunfo(posicion) is not None:
                return self.heuristica(posicion), posicion

            if max_player:
                max_eval = float('-inf')
                best = None

                for child in self.posiciones_siguientes(posicion):
                    eval, _ = minimax(child, depth - 1, False)

                    if eval > max_eval:
                        max_eval = eval
                        best = child

                return max_eval, best
            else:
                min_eval = float('inf')
                best = None

                for child in self.posiciones_siguientes(posicion):
                    eval, _ = minimax(child, depth - 1, True)

                    if eval < min_eval:
                        min_eval = eval
                        best = child

                return min_eval, best

        _, best = minimax(posicion, max_depth, True)

        return best
