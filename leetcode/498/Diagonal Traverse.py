from typing import List
from collections import defaultdict

# solution 1 - (defaultdict,hash_table) - (16ms) - (2025.08.25)
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        n = len(mat)
        m = len(mat[0])

        hash_table = defaultdict(list)

        for i in range(n):
            for j in range(m):
                hash_table[i + j].append(mat[i][j])

        # print(hash_table)
        answer = []
        for i, lst in hash_table.items():
            # print(*lst)
            if i % 2 == 0:
                answer.extend(lst[::-1])
            else:
                answer.extend(lst)

        return answer


# solution 2 - (matrix,enumeration) - (3ms) - (2025.08.25)
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        n = len(mat)
        m = len(mat[0])
        answer = []
        r = c = 0

        for _ in range(n * m):
            answer.append(mat[r][c])

            if (r + c) % 2 == 0:
                if c == m - 1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:
                if r == n - 1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1

        return answer
