#coding:utf-8
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
def solution(nums, target):
    my_map = {}
    for i, v in enumerate(nums):
        result = target - v
        map_value = my_map.get(result, None)
        if map_value or map_value == 0 :
            return [my_map[result], i]
        else:
            my_map[v] = i
    return None

print solution([3,3], 6)
