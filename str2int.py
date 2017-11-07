def solution(tempStr):
    if len(tempStr) == 0:
        return 0
    filterStr = ''
    for s in tempStr:
        if s != ' ':
            filterStr = filterStr + s
    result = ''
    for i, v in enumerate(filterStr):
        if v == '-' or v == '+':
            if i == 0:
                if len(filterStr) == 1:
                    return 0
                result = result + v
            elif i == 1:
                return 0

        elif ord('0') <= ord(v) <= ord('9'):
            result = result + v
            continue
        else:
            break
    return 0 if len(result) == 0 or (len(result) == 1 and (result == '+' or result == '-')) else int(result)

print solution("-abc")