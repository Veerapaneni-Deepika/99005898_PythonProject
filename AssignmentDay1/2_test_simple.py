from simple import add
from simple import fdiv, idiv
from simple import is_leap
from simple import factorial
from simple import is_prime

def test_simple_add():
    assert 30 == add(10,20)
    assert 40 == add(22,18)
    assert 15 == add(25,-10)
    assert 32 == add(-8, 40)
    
    
def test_simple_fdiv():
    assert 25 == fdiv(200,8)
    assert 4.5 == fdiv(45,10)


def test_simple_idiv():
    assert 25 == fdiv(200,8)
    assert 4 == idiv(45,10)

    
def test_leap_years():
    assert True == is_leap(1996)
    assert True == is_leap(2016)
    assert is_leap(2000)
    assert not is_leap(2100) 

   
def test_non_leap_years():
    assert False == is_leap(2015)
    assert False == is_leap(1995)


def test_leap_corner():             
    assert False == is_leap(1700)
    assert False == is_leap(1900)
    assert -1 == is_leap(-1990)
    

def test_factorial_general():
    assert 120 == factorial(5)
    assert 5040 == factorial(7)
    

def test_factorial_corner():
    assert 1 == factorial(0)
    assert 1 == factorial(1)
    assert -1 == factorial(-4)
    assert -1 == factorial(-8)
    
    
def test_prime_general():
    assert is_prime(17)
    assert is_prime(41)
    assert not is_prime(16)
    assert not is_prime(69)

    
def test_prime_corner():
    assert None==is_prime(0)
    assert None==is_prime(1)
    assert -1==is_prime(-5)
    assert -1==is_prime(-10)

