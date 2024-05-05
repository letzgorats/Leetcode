# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

# All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.
# Suppose i need to delete 6
# (ex) 4-> 5 -> 6 -> 7

# 7 -> val = 6 -> val
# 4-> 5 -> 6 -> 6'

# 6-> next = 6'-> next
# 6-> next = 6 -> next -> next

(cf : https://youtu.be/NRolW_6uHPE)
