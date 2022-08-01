import pytest
from src.calc import Caluculator

def test_first_step():
    assert (1,2,3) == (1,2,3)

def test_second_step():
    assert (3,2,1) == (3,2,1)

def test_sum():
    calculator = Caluculator()
    assert calculator.sum(1,2) == 3

def test_sub():
    calculator = Caluculator()
    assert calculator.sub(3,1) == 2

def test_sum_of_minus_value_case():
    calc = Caluculator()
    with pytest.raises(ValueError):
        assert calc.sum(-1,2)

@pytest.mark.skip(reason="skip test")
def test_sum_of_minus_value_case_skip_test():
    calc = Caluculator()
    with pytest.raises(ValueError):
        assert calc.add(-1,2)

@pytest.mark.parametrize('test_value',
                            [   (1,2,3),
                                (3,10,13),
                                (3,11,14)])
def test_sum_of_multi_case(test_value):
    calc = Caluculator()
    calc.sum(test_value[0],test_value[1]) == test_value[2]
    
@pytest.mark.parametrize('left, right, excepted',
                            [   (1,2,3),
                                (3,10,13),
                                (3,11,14)])
def test_sum_of_multi_case_two(left, right, excepted):
    calc = Caluculator()
    calc.add(left,right) == excepted

def test_sum_of_save(mocker):
    mock = mocker.patch("src.calc.FileRepository.save")
    
    calc = Caluculator()
    calc.save(123)

    mock.assert_called_once()

    mock.assert_called_with("result.txt", 123)