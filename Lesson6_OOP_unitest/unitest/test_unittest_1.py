import unittest
from unittest import TestCase

from Lesson6_OOP_unitest.unitest.unitest_1 import Calculator


class TestCalculator(TestCase):
    def test_add(self):
        calculator = Calculator()

        self.assertEqual(5, calculator.add(2,3))
        self.assertEqual(4, calculator.add(2,3))

        # self.assertEqual(calculator.add(2,3),5)
        # self.assertEqual(calculator.add(2, 3), 4)