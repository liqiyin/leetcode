# -*- coding: utf-8 -*-
def solution(s):
    curLen = 0
    maxLen = curLen
    for i, v in enumerate(s):
        j = 0
        #奇数拓展
        while i - j >= 0 and i + j < len(s):
            if s[i - j] == s[i + j]:
                curLen = j * 2 + 1
                if curLen > maxLen:
                    maxLen = curLen
            else:
                break
            j += 1

        j = 0
        while i - j >= 0 and i + j - 1 < len(s):
            if s[i - j] == s[i + j - 1]:
                curLen = j * 2
                if curLen > maxLen:
                    maxLen =curLen
            else:
                break
            j += 1
    return maxLen

print solution("abccccccd")