import re

def solution(n):
    bin_num = bin(n)[2:]
    regex = re.findall(r"1(0+)1", bin_num)
    regex1 = re.findall(r"1(0+)1", bin_num[::-1])
    regex += regex1 
    if regex:
        result = max(map(len, regex))
    else:
        result = 0
    return result