#coding:utf-8
#Write a function to find the longest common prefix string amongst an array of strings.
#求一个数组列表的最长公共前缀
#[abc, abcd, abcdadj, ab]  -> 'ab'
def solution(strs):
    if len(strs) == 0:
        return ''

    if len(strs) == 1:
        return strs[0]

    result = ''
    for i, v in enumerate(strs[0]):
        temp = v
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != temp:
                return result
        result += temp
    return result
