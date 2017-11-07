# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321

def solution(integer):
    maxSize = 1 << 31
    tempStr = str(integer)
    hasSigned = tempStr.startswith("-")
    tempStr = tempStr[:0:-1] if hasSigned else tempStr[::-1]
    result = int(tempStr)
    if result > maxSize:
        return 0
    return -result if hasSigned else result

print solution(1534236469)