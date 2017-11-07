# PAYPALISHIRING

# P   A   H   N
# A P L S I I G
# Y   I   R

# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

def convert(s, row):
    if row == 1:
        return s
    result = []
    for i in range(row):
        result.append("")

    maxNum = row - 1
    cur = 0
    isMinius = False
    for temp in s:
        result[cur] += temp

        if cur == 0:
            isMinius = False
        if cur == maxNum:
            isMinius = True

        if isMinius:
            cur -= 1
        else:
            cur += 1
        print cur

    print result
    resultStr = ""
    for i, v in enumerate(result):
        resultStr += v
    return resultStr
print convert("ABC", 2)
