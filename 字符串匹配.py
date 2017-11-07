# -*- coding: utf-8 -*-
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true

def solution(s, p):
    if not p:
        return not s

    find_match = bool(s) and p[0] in {s[0], "."}

    if len(p) >= 2 and p[1] == '*':
        #当前字符不匹配 'a*'样式 或者 匹配这个样式
        return solution(s, p[2:]) or (find_match and solution(s[1:], p))
    else:
        return find_match and solution(s[1:], p[1:])

print solution("aa", ".*")