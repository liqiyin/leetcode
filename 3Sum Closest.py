# coding:utf-8
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.
#  You may assume that each input would have exactly one solution.
#
# For example, given array S = {-1 2 1 -4}, and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
import math


def solution(arr, target):
    arr = sorted(arr)
    minNum = arr[0] + arr[1] + arr[2]
    for i in range(0, len(arr) - 2):
        v = arr[i]
        k = twoSum(arr[i + 1: len(arr)], target - v)
        if k + v == target:
            return target
        if math.fabs(minNum - target) > math.fabs(k + v - target):
            minNum = k + v
    return minNum


def twoSum(arr, target):
    i = 0
    j = len(arr) - 1
    minNum = arr[i] + arr[j]
    if len(arr) == 2:
        return minNum
    while i < j and j > 0 and i < len(arr):
        temp = arr[i] + arr[j]
        if temp - target == 0:
            return target
        if math.fabs(minNum - target) > math.fabs(temp - target):
            minNum = temp

        if temp < target:
            i += 1
        else:
            j -= 1

    return minNum


print solution([1,-3,3,5,4,1], 1)
