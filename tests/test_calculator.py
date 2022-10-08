from calculator import Calculator
import pytest

class Test_calc:
    def setup(self):
        self.calculator = Calculator

    def test_mulstiply_correct(self):
        assert self.calculator.multiply(self,10,55) == 550

    def test_mulstiply_negativ(self):
        assert self.calculator.multiply(self, 0, 55) == 1

    def test_division_correct(self):
        assert self.calculator.division(self,55,5) == 11

    def test_division_negativ(self):
        assert self.calculator.division(self, 0, 55) == 1

    def test_subtraction_correct(self):
        assert self.calculator.subtraction(self, 55, 5) == 50

    def test_subtraction_negativ(self):
        assert self.calculator.subtraction(self, 0, 55) == 1

    def test_adding_correct(self):
        assert self.calculator.adding(self, 55, 5) == 60

    def test_adding_negativ(self):
        assert self.calculator.adding(self, 0, 55) == 1
