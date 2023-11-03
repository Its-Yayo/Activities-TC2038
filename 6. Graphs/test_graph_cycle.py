#!/usr/bin/env python3

from unittest import TestCase, main
from graph_cycle import has_cycle


class TestGraphCycle(TestCase):

    def test_has_cycle_1(self):
        self.assertIsNone(
            has_cycle('A', {
                'A': ['B'],
                'B': ['A']
            }))

    def test_has_cycle_2(self):
        self.assertIsNone(
            has_cycle('A', {
                'A': ['B'],
                'B': ['A', 'C'],
                'C': ['B']
            }))

    def test_has_cycle_3(self):
        self.assertEqual(
            ['A', 'B', 'C', 'A'],
            has_cycle('A', {
                'A': ['B', 'C'],
                'B': ['A', 'C'],
                'C': ['A', 'B']
            }))

    def test_has_cycle_4(self):
        self.assertIsNone(
            has_cycle('C', {
                'A': ['B'],
                'B': ['A', 'C'],
                'C': ['B', 'D'],
                'D': ['C'],
            }))

    def test_has_cycle_5(self):
        self.assertEqual(
            ['B', 'A', 'C', 'B'],
            has_cycle('D', {
                'A': ['B', 'C'],
                'B': ['A', 'C', 'D'],
                'C': ['A', 'B', 'E'],
                'D': ['B', 'E'],
                'E': ['C', 'D']
            }))

    def test_has_cycle_6(self):
        self.assertEqual(
            ['B', 'C', 'E', 'D', 'B'],
            has_cycle('A', {
                'A': ['B'],
                'B': ['A', 'C', 'D'],
                'C': ['B', 'E'],
                'D': ['B', 'E'],
                'E': ['C', 'D']
            }))

    def test_has_cycle_7(self):
        self.assertEqual(
            ['D', 'C', 'E', 'D'],
            has_cycle('A', {
                'A': ['B'],
                'B': ['A', 'D'],
                'C': ['D', 'E'],
                'D': ['C', 'E'],
                'E': ['C', 'D']
            }))

    def test_has_cycle_8(self):
        self.assertIsNone(
            has_cycle('E', {
                'A': ['B'],
                'B': ['A', 'D'],
                'C': ['D'],
                'D': ['B', 'C', 'E'],
                'E': ['D']
            }))

    def test_has_cycle_9(self):
        self.assertEqual(
            ['B', 'A', 'C', 'D', 'B'],
            has_cycle('B', {
                'A': ['B', 'C'],
                'B': ['A', 'D'],
                'C': ['A', 'D'],
                'D': ['B', 'C', 'E'],
                'E': ['D']
            }))

    def test_has_cycle_10(self):
        self.assertEqual(
            ['A', 'B', 'C', 'A'],
            has_cycle('D', {
                'A': ['B', 'C', 'D'],
                'B': ['A', 'C', 'D'],
                'C': ['A', 'B', 'D', 'E'],
                'D': ['A', 'B', 'C', 'E'],
                'E': ['C', 'D']
            }))

    def test_has_cycle_11(self):
        self.assertEqual(
            ['A', 'B', 'D', 'A'],
            has_cycle('E', {
                'A': ['B', 'C', 'D'],
                'B': ['A', 'D'],
                'C': ['A', 'D', 'E'],
                'D': ['A', 'B', 'C', 'E'],
                'E': ['C', 'D']
            }))

    def test_has_cycle_12(self):
        self.assertEqual(
            ['E', 'C', 'A', 'B', 'D', 'E'],
            has_cycle('E', {
                'A': ['B', 'C'],
                'B': ['A', 'D'],
                'C': ['A', 'E'],
                'D': ['B', 'E'],
                'E': ['C', 'D']
            }))

    def test_has_cycle_13(self):
        self.assertEqual(
            ['D', 'E', 'F', 'D'],
            has_cycle('A', {
                'A': ['B'],
                'B': ['A', 'C'],
                'C': ['B', 'D'],
                'D': ['C', 'E', 'F'],
                'E': ['D', 'F'],
                'F': ['D', 'E']
            }))

    def test_has_cycle_14(self):
        self.assertEqual(
            ['D', 'C', 'E', 'D'],
            has_cycle('F', {
                'A': ['B'],
                'B': ['A', 'D'],
                'C': ['D', 'E'],
                'D': ['B', 'C', 'E', 'F'],
                'E': ['C', 'D', 'F'],
                'F': ['D', 'E']
            }))

    def test_has_cycle_15(self):
        self.assertEqual(
            ['E', 'C', 'I', 'H', 'G', 'F', 'D', 'E'],
            has_cycle('B', {
                'A': ['D'],
                'B': ['E'],
                'C': ['E', 'I'],
                'D': ['A', 'E', 'F'],
                'E': ['B', 'C', 'D'],
                'F': ['D', 'G'],
                'G': ['F', 'H'],
                'H': ['G', 'I'],
                'I': ['C', 'H']
            }))

    def test_has_cycle_16(self):
        self.assertEqual(
            ['C', 'I', 'H', 'C'],
            has_cycle('A', {
                'A': ['D'],
                'B': ['E'],
                'C': ['E', 'I', 'H'],
                'D': ['A', 'E', 'F'],
                'E': ['B', 'C', 'D'],
                'F': ['D', 'G'],
                'G': ['F', 'H'],
                'H': ['C', 'G', 'I'],
                'I': ['C', 'H']
            }))

    def test_has_cycle_17(self):
        self.assertIsNone(
            has_cycle('A', {
                'A': ['D'],
                'B': ['E'],
                'C': ['E', 'I'],
                'D': ['A', 'E', 'F'],
                'E': ['B', 'C', 'D'],
                'F': ['D'],
                'G': ['H'],
                'H': ['G', 'I'],
                'I': ['C', 'H']
            }))

    def test_has_cycle_18(self):
        self.assertEqual(
            ['A', 'B', 'C', 'A'],
            has_cycle('D', {
                'A': ['B', 'C', 'D', 'E'],
                'B': ['A', 'C', 'D', 'E'],
                'C': ['A', 'B', 'D', 'E'],
                'D': ['A', 'B', 'C', 'E'],
                'E': ['A', 'B', 'C', 'D']
            }))

    def test_has_cycle_19(self):
        self.assertEqual(
            ['A', 'C', 'E', 'A'],
            has_cycle('B', {
                'A': ['B', 'C', 'D', 'E'],
                'B': ['A'],
                'C': ['A', 'E'],
                'D': ['A'],
                'E': ['A', 'C']
            }))

    def test_has_cycle_20(self):
        self.assertEqual(
            ['F', 'E', 'D', 'C', 'I', 'H', 'G', 'F'],
            has_cycle('F', {
                'A': ['B'],
                'B': ['A', 'C'],
                'C': ['B', 'D', 'I'],
                'D': ['C', 'E'],
                'E': ['D', 'F'],
                'F': ['E', 'G'],
                'G': ['F', 'H'],
                'H': ['G', 'I'],
                'I': ['C', 'H'],
            }))


if __name__ == '__main__':
    main()