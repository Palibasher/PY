from app import calculator
import pytest

class Test_calc:
    def setup(self):
        self.calc = calculator

    def test_mulstiply_correct(self):
        assert self.calculator.myltiple(self,10,55) == 550

    def test_mulstiply_negativ(self):
        assert self.calculator.myltiple(self, 0, 55) == 1