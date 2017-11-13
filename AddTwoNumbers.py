#coding:utf-8
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def solution(self, n1, n2):
        n3 = result = None
        extra = 0
        while n1 or n2 or extra != 0:
            sum = (n1.val if n1 else 0) + (n2.val if n2 else 0) + extra
            temp = ListNode(sum % 10)
            extra = sum / 10
            if n3:
                n3.next = temp
                n3 = n3.next
            else:
                n3 = temp
                result = n3
            n1 = n1.next if n1 else None
            n2 = n2.next if n2 else None
        return result

node = Solution().solution(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
while node:
    print node.val
    node = node.next