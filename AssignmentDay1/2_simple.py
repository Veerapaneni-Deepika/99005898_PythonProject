'''
This is the source code for all functions
'''

def add(num1, num2):
    'fn to add'
    return num1 + num2

def fdiv(num1, num2):
    'fn to do float div'
    return num1/num2

def idiv(num1, num2):
    'fn to do integer div'
    return num1//num2

def is_leap(year):
    'fn to check leap yr'
    if year<0:
        return -1
    return year%400==0 or year%4==0 and year%100!=0

def factorial(num):
    'fn to calculate factorial'
    fact=1
    if num<0:
        return -1
    for i in range(num,0,-1):
        fact=fact*i
    return fact

def is_prime(num):
    'fn to check prime number'
    flag=True
    if num<0:
        return -1
    if num in (0,1):
        return None
    for i in range(2,num-1):
        if num%i==0:
            flag=False
    return flag
