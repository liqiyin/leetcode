#coding:utf-8
# Given n non-negative integers a1, a2, ..., an,
# where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2

def solution(height):
    if len(height) < 2:
        return 0
    left = 0
    right = len(height) - 1
    maxSize = 0
    while left < right:
        maxSize = max(maxSize, (right - left) * min(height[left], height[right]))
        if height[left] > height[right]:
            right = right - 1
        else:
            left = left + 1
    return maxSize
