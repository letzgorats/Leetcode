# my solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 우 하 좌 상
        matrix = [[-1] * n for _ in range(m)]
        cur_dir = 0
        curr, curc = 0, 0
        visit = set()
        visit.add((curr, curc))
        matrix[0][0] = head.val
        head = head.next

        for _ in range(n * m - 1):

            if head is None:
                break

            nr = curr + direction[cur_dir][0]
            nc = curc + direction[cur_dir][1]
            if nr < 0 or nr >= m or nc < 0 or nc >= n or (nr, nc) in visit:
                cur_dir = (cur_dir + 1) % 4
                nr = curr + direction[cur_dir][0]
                nc = curc + direction[cur_dir][1]

            curr, curc = nr, nc
            visit.add((curr, curc))
            matrix[curr][curc] = head.val
            head = head.next

        return matrix

# different solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        matrix = [[-1] * n for _ in range(m)]
        top, bottom, left, right = 0, m - 1, 0, n - 1
        curr = head

        while top <= bottom and left <= right and curr:

            # move right
            for i in range(left, right + 1):
                if curr:
                    matrix[top][i] = curr.val
                    curr = curr.next
            top += 1

            # move down
            for i in range(top, bottom + 1):
                if curr:
                    matrix[i][right] = curr.val
                    curr = curr.next
            right -= 1

            # move left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    if curr:
                        matrix[bottom][i] = curr.val
                        curr = curr.next
                bottom -= 1

            # move up
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    if curr:
                        matrix[i][left] = curr.val
                        curr = curr.next
                left += 1

        return matrix