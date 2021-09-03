'''
This is the test code
'''
from simple import add
from simple import multiply
from simple import even
from simple import odd

def test_add():
    assert 5==add(2, 3)
    assert 10==add(20,-10)

def test_multiply():
    assert 6==multiply(2, 3)
    assert -200==multiply(20,-10)

def test_even():
    assert True==even(0)
    assert False==even(-3)

def test_odd():
    assert True==odd(101)
    assert False==odd(0)