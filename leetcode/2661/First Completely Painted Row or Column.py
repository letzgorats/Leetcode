# soultion 1 - += 활용
from collections import defaultdict
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        n, m = len(mat), len(mat[0])

        pos = defaultdict(int)

        for i in range(n):
            for j in range(m):
                pos[mat[i][j]] = (i, j)

        # visited = [[False] * m for _ in range(n)]

        rows = [0 for i in range(n)]
        cols = [0 for j in range(m)]

        for idx, num in enumerate(arr):

            r, c = pos[num]
            # visited[r][c] = True
            rows[r] += 1
            cols[c] += 1

            if rows[r] == m or cols[c] == n:
                return idx

        return -1

'''
+= 와 같은 합을 이용해서 총합이 m인지 n인지를 판단함으로써
1차원 배열에서도 2차원 배열의 visited 여부를 확인할 수 있게 된다.
'''

# TLE
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        n, m = len(mat), len(mat[0])

        pos = defaultdict(int)

        for i in range(n):
            for j in range(m):
                pos[mat[i][j]] = (i, j)

        visited = [[False] * m for _ in range(n)]

        # rows = [0 for i in range(n)]
        # cols = [0 for j in range(m)]

        for idx, num in enumerate(arr):

            r, c = pos[num][0], pos[num][1]
            visited[r][c] = True

            # row check
            for j in range(m):
                if not visited[r][j]:
                    break
            else:
                return idx
            # col check
            for i in range(n):
                if not visited[i][c]:
                    break
            else:
                return idx

        return -1
