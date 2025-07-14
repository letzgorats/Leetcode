# solution 1 - (linked list) - (0ms) - (2025.07.14)
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        answer = 0
        while head:
            answer = answer * 2 + head.val
            head = head.next

        return answer
