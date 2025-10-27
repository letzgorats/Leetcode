# solution 3 - (array,math,string) - (100ms) - (2025.10.27)
from collections import defaultdict
from typing import List
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        laser = []
        for i, b in enumerate(bank):
            cnt = 0
            for idx, j in enumerate(b):
                if j == '1':
                    cnt += 1
            if cnt:
                laser.append(cnt)

        ans = 0
        for i in range(len(laser) - 1):
            ans += (laser[i] * laser[i + 1])

        return ans

# solution 1 - (math,string) - (117ms) - (2024.07.03)
class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        cur, pre = 0, 0
        answer = 0
        for i in bank:

            cur = i.count('1')
            if cur :
                answer += (pre * cur)
                pre = cur

        return answer

# solution 1 - (matrix,array) - (999ms) - (2024.07.03)
class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """

        board = []
        for row in bank:
            if '1' in row:  
                board.append(list(map(int,row)))

        n = len(board)

        answer = 0
        for i in range(n-1):
            a = board[i].count(1)
            b = board[i+1].count(1)
            answer += (a*b)

        return answer
        
