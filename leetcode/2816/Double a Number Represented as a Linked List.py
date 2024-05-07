# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current = head
        prev = None

        while current:
            
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        head = prev
        carry = 0
        current = head
        prev = None
        
        while current:
            # 현재 노드 값에 2배를 곱하고 자리올림 값을 더함.
            doubled = 2 * current.val + carry
            # 두 배한 값에서 10으로 나눈 나머지를 현재 노드 값으로 설정
            current.val = doubled % 10
            # 나눗셈의 몫을 다음 자리의 올림수로 설정
            carry = doubled // 10
            # 마지막 노드에 대한 참조를 업데이트
            prev = current
            # 다음 노드로 이동
            current = current.next
        
        # 마지막 노드 처리 후 자리올림 값이 남아있으면 새 노드 추가
        if carry:
            prev.next = ListNode(carry)
        
        prev = None
        current = head
        while current :
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
       
        return prev
