# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """

        answer = []
        i = 1
        mini, maxi = 0, 0
        prev = head
        current = prev.next

        while current != None:

            if current.val == prev.val:
                mini, maxi = 0, 0

            elif current.val < prev.val:
                if mini == 1:
                    mini = 1
                elif mini == 0:
                    mini += 1

                if maxi == 1:
                    answer.append(i)
                    maxi = 0

            elif current.val > prev.val:
                if maxi == 1:
                    maxi = 1
                elif maxi == 0:
                    maxi += 1
                if mini == 1:
                    answer.append(i)
                    mini = 0

            prev = current
            current = prev.next
            i += 1

        if len(answer) <= 1:
            return [-1, -1]
        min_diff = int(1e9)
        for i in range(len(answer) - 1):
            min_diff = min(answer[i + 1] - answer[i], min_diff)

        max_diff = answer[-1] - answer[0]

        return [min_diff, max_diff]
