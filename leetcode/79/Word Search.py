# dfs solution
class Solution(object):
    def exist(self, board, word):


        def dfs(r,c,index):

            if index == len(word): # 단어를 끝까지 찾음
                return True

            elif r < 0 or r >= n or c < 0 or c >= m or word[index] != board[r][c]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"

            found = dfs(r-1,c,index+1) or dfs(r+1,c,index+1) \
                    or dfs(r,c-1,index+1) or dfs(r,c+1,index+1)

            board[r][c] = temp      

            return found      

        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            for j in range(m):
                if dfs(i,j,0):
                    return True
        
        return False
    

# wrong solution - bfs
from collections import deque

class Solution(object):
    def exist(self, board, word):

        def bfs(r,c,deq):

            queue = deque([(r,c)])
            
            dr = [-1,1,0,0]
            dc = [0,0,-1,1]
            visited = [[False] * m for _ in range(n)]
            visited[r][c] = True

            while queue:
                if len(deq) == 0:
                    return True

                w = deq.popleft()
                r, c = queue.popleft()
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    
                    if 0<= nr < n and 0 <= nc < m and not visited[nr][nc]:
                        if board[nr][nc] == w:
                            queue.append((nr,nc))
                            visited[nr][nc] = True
                        

            return False

        
        start = word[0]
        start_point = deque([])
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            for j in range(m):
                if start == board[i][j]:
                    start_point.append((i,j))
        
        while start_point:
            
            deq = deque(list(word[1:]))
            i, j = start_point.popleft()
            if bfs(i,j,deq):
                return True
        
        return False
