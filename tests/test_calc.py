from src.calc import Caluculator

class TestClassCalc():
    def test_sum(self):
        calculator = Caluculator()
        assert calculator.sum(1,2) == 3
        assert calculator.sum(-2,1) == -1
        
    def test_sub(self):
        calculator = Caluculator()
        assert calculator.sub(3,1) == 2
        