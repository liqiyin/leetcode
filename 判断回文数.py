"""
1.负数不是回文数
"""
def solution(num):
    if num < 0 or (num % 10 == 0 and num != 0):
        return False
    elif num < 10:
        return True

    reverseNum = 0
    while num > reverseNum:
        reverseNum = reverseNum * 10 + num % 10
        num = int(num / 10)

    return reverseNum == num or int(reverseNum / 10) == num