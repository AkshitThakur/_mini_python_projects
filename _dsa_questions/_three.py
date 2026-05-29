# Program to find the even factor sum of a number. 

#18 = > 2, 3, 6, 9, 18, = > 2+6+18 = 26

"""#complexity : O(n)
def sum_of_even_factors(_num):
    _sum = 0
    for i in range(1, _num+1):
        if _num%i==0 and i%2==0:
            _sum += i
    return _sum
_result = sum_of_even_factors(18)
print(_result)"""

"""#complexity : O(n/2)
def sum_of_even_factors(_num):
    _sum = sum(i for i in range(2, _num+1, 2) if _num%i==0)
    return _sum
_result = sum_of_even_factors(18)
print(_result)"""


#complexity : O(under root of n)
def sum_of_even_factors(_num):
    _sum = 0
    for i in range(2, int(_num**0.5)+1):#2,3,4
        if _num%i==0 and i%2==0:
            _sum += i#2
        _pair = _num//i#2->9, 3->6
        if _pair != i and _pair%2==0:
            _sum += _pair#6
    if _num%2==0:
        _sum += _num#18
    return _sum

_result = sum_of_even_factors(18)
print(_result)