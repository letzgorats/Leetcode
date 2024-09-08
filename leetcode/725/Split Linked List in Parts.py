# solution 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        curr = head
        length = 0
        while curr:
            prev = curr
            curr = curr.next
            length += 1

        part_size = length // k
        extra_size = length % k

        answer = [part_size + 1] * extra_size + [part_size] * (k - extra_size)

        prev, curr = None, head
        for idx, num in enumerate(answer):
            if prev:
                prev.next = None
            answer[idx] = curr
            for i in range(num):
                prev, curr = curr, curr.next

        return answer


# solution 2
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

            length = 0
            while curr:
                prev = curr
                curr = curr.next
                length += 1

            part_size = length // k
            extra_size = length % k

            curr = head
            answer = []

            for i in range(k):

                part_head = curr
                for j in range(part_size - 1 + (i < extra_size)):
                    if curr:
                        curr = curr.next
                if curr:
                    next_node = curr.next
                    curr.next = None
                    curr = next_node
                answer.append(part_head)

            return answer