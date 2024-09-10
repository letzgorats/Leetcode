# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def gcd(a, b):

            while b:
                a, b = b, a % b
            return a

        curr = head

        while curr and curr.next:
            gcd_val = gcd(curr.val, curr.next.val)
            new_node = ListNode(gcd_val)

            # Insert New Node between curr and curr.next
            new_node.next = curr.next
            curr.next = new_node

            # move to the next pair (skip the inserted node)
            curr = new_node.next

        return head
