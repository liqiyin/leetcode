# coding=utf-8
# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note: The solution set must not contain duplicate quadruplets.
#
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#     [-1,  0, 0, 1],
#     [-2, -1, 1, 2],
#     [-2,  0, 0, 2]
# ]

def fourSum(nums, target):
    lastNum = None
    nums = sorted(nums)
    result = []
    for i, v in enumerate(nums):
        if v == lastNum:
            continue
        arr = threeSum(nums[i + 1:], target - v)
        if arr:
            for a in arr:
                a.append(v)
                result.append(a)
        lastNum = v
    return result


def threeSum(nums, target):
    result = []
    temp = []
    for i, v in enumerate(nums):
        if v in temp:
            continue
        else:
            temp.append(v)
            resultArr = twoSum(nums[i + 1:], target - v)
            if resultArr:
                for arr in resultArr:
                    arr.append(v)
                    result.append(arr)
    return result


def twoSum(nums, target):
    result = []
    map = {}
    for i, v in enumerate(nums):
        if target - v in map:
            if v in map:
                if v == target - v and map[v] == 0:
                    result.append([target - v, v])
                    map[v] += 1
                continue
            else:
                result.append([target - v, v])
                map[v] = 0
        else:
            map[v] = 0
    return result

print fourSum([1, 0, -1, 0, -2, 2], 0)
