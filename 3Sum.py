#coding:utf-8
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]
import time
def solution(nums):
    result = []
    temp = []
    # 去重关键 先对数组进行排序
    t = time.time()
    nums = sorted(nums)
    for i, v in enumerate(nums):
        if v in temp:
            continue
        else:
            temp.append(v)
            resultArr = twoSum(nums[i + 1:], -v)
            if resultArr:
                for arr in resultArr:
                    arr.append(v)
                    result.append(arr)
    print time.time() - t
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

print solution([-15,6,7,0,-14,-5,-3,-10,-14,1,-14,-1,-11,-11,-15,-1,3,-12,7,14,1,6,-6,7,1,1,0,-4,8,7,2,1,-2,-6,-14,-9,-3,-1,-12,-2,7,11,4,12,-14,-4,-4,4,-1,10,3,-14,1,12,0,10,-9,8,-9,14,-8,8,0,-3,10,-6,4,-8,0,-1,-3,-8,-4,8,11,-3,-11,-8,8,3,10,-3,-4,-4,-14,12,13,-8,-3,12,-8,4,5,-1,-14,-8,8,-3,-9,-15,12,-5,-7,-15,-12,11,-11,14,11,12,3,6,-6])
