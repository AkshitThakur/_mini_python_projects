# Program to find the most repeated character and its count in a string/word

"""from collections import Counter
_str = "helloworld"
_result = Counter(_str).most_common()[0]
print(_result)"""

"""
_str = "helloworld"
def most_repeated_char(_str):
    _char_dict = {}
    for _chr in _str:
        _char_dict[_chr] = _char_dict.get(_chr, 0)+1
    _repeated_char = max(_char_dict, key=_char_dict.get)
    print(_repeated_char, _char_dict[_repeated_char])
most_repeated_char(_str)"""

_str = "helloworld"
def most_repeated_char(_str):
    _char_dict = {}
    _repeated_char = ""
    _char_count = 0
    for _chr in _str:
        _char_dict[_chr] = _char_dict.get(_chr, 0)+1
        if _char_dict[_chr]>_char_count:
            _char_count = _char_dict[_chr]
            _repeated_char = _chr
    print(_repeated_char, _char_count)

most_repeated_char(_str)