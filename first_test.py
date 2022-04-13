import pytest
from app.calculator import Calculator

class Testcalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 20, 5) == 100

    def test_addition_calculate_correctly(self):
        assert self.calc.addition(self, 20, 5) == 4

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 20, 5) == 25

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 20, 5) == 15
