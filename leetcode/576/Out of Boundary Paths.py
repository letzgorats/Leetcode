from collections import deque

class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """

        mod = 10 ** 9 + 7
        # 메모이제이션을 위한 3차원 리스트 초기화
        memo = [[[None for _ in range(maxMove + 1)] for _ in range(n)] for _ in range(m)]
        dr = [-1,1,0,0] # 상 하 좌 우   
        dc = [0,0,-1,1] # 상 하 좌 우  

        def bfs(r,c,maxMove):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 1

            if maxMove == 0:
                return 0

            if memo[r][c][maxMove] is not None:
                return memo[r][c][maxMove]

            cnt = 0
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                cnt = (cnt + bfs(nr, nc, maxMove - 1)) % mod

            memo[r][c][maxMove] = cnt
            return cnt

        return bfs(startRow, startColumn, maxMove)

        # def bfs(r,c):

        #     move = 0 
        #     queue = deque([])
        #     queue.append((r,c,move))
        #     cnt = 0 

        #     while queue:
                
        #         r,c,move = queue.popleft()
        
        #         if move < maxMove:
        #             for d in range(4):
                        
        #                 nr = r + dr[d]
        #                 nc = c + dc[d]
        #                 # 경계 체크
        #                 if nr < 0 or nr >= m or nc < 0 or nc >= n:
        #                     cnt = (cnt + 1) % mod
        #                 else:
        #                     # 중복 방문 방지
        #                     if memo[nr][nc][move+1] is None:
        #                         queue.append((nr, nc, move+1))
        #                         memo[nr][nc][move+1] = True
        

        #     return cnt

        
        # return bfs(startRow,startColumn)
        


        
