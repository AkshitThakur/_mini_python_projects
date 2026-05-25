#1. Program for Check if number is divisible by its digits

# def check_divisibility(_num):
#     for i in str(_num):
#         if int(i)==0 or _num%int(i)!=0:
#             return "NO"
#     return "YES"

def check_divisibility(_num):
    return "Yes" if all(int(i)!=0 and _num%int(i)==0 for i in str(_num)) else "no"

_result = check_divisibility(128)
print(_result)
