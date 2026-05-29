# Given a number n, the task is to find the even factor sum of a number. 

#complexity = n/2
"""def sum_of_even_factors(_num):
    _factors_sum = (sum(i for i in range(2,_num+1,2) if _num%i==0))
    return _factors_sum
_val = sum_of_even_factors(18)
print(_val)"""

#complexity : under root n
def sum_of_even_factors(_num):
    _factors_sum = 0
    for i in range(2, int(_num**0.5)+1):
        if _num%i==0 and  i%2==0:
            _factors_sum += i
        _pair = _num//i
        if i != _pair and _pair%2==0:
            _factors_sum += _pair
    if _num%2==0:
        _factors_sum += _num
    return _factors_sum
_val = sum_of_even_factors(18)
print(_val)

#complexity : n
"""def sum_of_even_factors(_num):
    _factors_sum = 0
    for i in range(1, _num+1):
        if _num%i == 0 and i%2==0:
            _factors_sum += i
    return _factors_sum
_val = sum_of_even_factors(18)
print(_val)"""