# Python Program to find smallest K-digit number divisible by X.
#83 => 10000
#83*120 = 9960
#83*121 = 10043


"""def k_digit(K, X):
    _small_k_digit_num = 10**(K-1) #10000
    _rem = _small_k_digit_num%X #40
    _small_k_digit_num += X-_rem
    return _small_k_digit_num"""

def k_digit(K, X):
    _small_k_digit_num = 10**(K-1)
    return (
        _small_k_digit_num + (-_small_k_digit_num%X)#rem = 43
    )

_result = k_digit(5, 83)
print(_result)