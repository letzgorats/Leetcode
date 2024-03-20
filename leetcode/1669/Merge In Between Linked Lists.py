# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """

        curr = list1

        i = 0

        while i < a-1:
            curr = curr.next
            i += 1
        # a = 3 , b = 4

        # 0 1 2 [3 4] 5 6 7

        head = curr
        # print(head)

        while i <= b:
            curr = curr.next
            i += 1
        
        head.next = list2

        while list2.next:
            list2 = list2.next
        list2.next = curr

        return list1





# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """

        ptr = list1
        for _ in range(a-1):
            ptr = ptr.next

        qtr = ptr.next

        for _ in range(b-a+1):
            qtr = qtr.next
        
        ptr.next = list2

        while list2.next:
            list2 = list2.next
        
        list2.next = qtr

        return list1


