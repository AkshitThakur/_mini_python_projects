#2. Program to find the possible values that X can for given modular equation (A mod X) = B holds good.

def check_values(A, B):
    _count = 0
    for  i in  range(1, A+1):
        if A%i == B:
            _count += 1
    return _count

A, B = 26, 2
_result = check_values(A, B)
print(_result)