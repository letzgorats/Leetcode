# solution 3 - (ListNode,set) - (50ms) - (2025.11.01)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        values_to_remove = set(nums)

        while head and head.val in values_to_remove:
            head = head.next

        if not head:
            return None

        current = head
        # print(head)
        while current.next:

            if current.next.val in values_to_remove:
                # skip
                current.next = current.next.next
            else:
                current = current.next

            # print(current)

        return head


# solution 1 - (design,ListNode) - (715ms) - (2024.09.06)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        nums = set(nums)
        dummy = ListNode(0)
        dummy.next = head

        prev, curr = dummy, head
        while curr:
            if curr.val in nums:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next

# solution 2 - (design,ListNode) - (745ms) - (2024.09.06)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        nums = set(nums)

        while head and head.val in nums:
            head = head.next

        if not head:
            return None

        prev = head
        curr = head.next

        while curr:
            if curr.val not in nums:
                prev.next = curr
                prev = curr
            curr = curr.next

        prev.next = None

        return head

