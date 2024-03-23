# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        

        fast = slow = head
    
        stack = []

        if not head: return []

        # find middle
        while fast.next and fast.next.next:
            
            slow = slow.next
            fast = fast.next.next
        

        # reverse second half
        prev, curr = None, slow.next
       
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        slow.next = None
        # print(slow)
        # print(fast)

        # merge first_half & second_half
        # print(prev)
        head1, head2 = head, prev
        while head1 and head2:
            next1 = head1.next
            next2 = head2.next

            head1.next = head2
            head1 = next1

            head2.next = head1
            head2 = next2
        
        # return hed

