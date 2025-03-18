import math
import pytest

@pytest.mark.sqrt
def test_sqrt():
    num =25
    assert math.sqrt(num) == 5

@pytest.mark.sqr
@pytest.mark.xfail
def testsquare():
    num = 7
    assert 7*7 == 40

@pytest.mark.skip
@pytest.mark.eql
def testequality():
    assert 10 ==11

#use fixture from conftest.py
def test_divisible_3(input_value):
    assert input_value % 3 ==0

def test_divisible_10(input_value):
    assert input_value % 10 ==0

# parameterizing
@pytest.mark.parametrize("num,output",[(1,11),(2,22),(3,35)])
def test_multiple_11(num,output):
    assert 11*num == output