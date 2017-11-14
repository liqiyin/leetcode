# coding:utf-8
# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 思路: 碰到重复的字母 一直删除到出现该字母位置的地方
def solution(s):
    result = []
    maxLength = 0
    for i, v in enumerate(s):
        if v in result:
            maxLength = len(result) if len(result) > maxLength else maxLength
            result = result[result.index(v) + 1: len(result)]
        result.append(v)
    return len(result) if len(result) > maxLength else maxLength
print solution("abba")
