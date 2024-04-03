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
    

# bfs solution - TLE
from collections import deque

class Solution:
    def exist(self, board, word):
        if not board:
            return False
        n, m = len(board), len(board[0])
        
        # 주어진 위치와 단어의 인덱스에서 시작하여 word를 찾을 수 있는지 확인하는 BFS 함수
        def bfs(r, c):
            queue = deque([(r, c, 0, {(r, c)})])  # (현재 행, 현재 열, 단어의 인덱스, 방문한 위치 집합)
            while queue:
                r, c, index, visited = queue.popleft()
                if index == len(word) - 1:
                    return True
                # 상하좌우 탐색
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited and board[nr][nc] == word[index + 1]:
                        new_visited = visited | {(nr, nc)}  # 현재 위치 추가
                        queue.append((nr, nc, index + 1, new_visited))
            return False
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:  # 단어의 첫 글자와 일치하는 모든 칸에서 BFS 시작
                    if bfs(i, j):
                        return True
        
        return False

# bfs solution - pass
class Solution:
    def exist(self, board, word):
        
        n, m = len(board), len(board[0])
        adj = [(0,-1), (0,1), (1,0), (-1,0)]
        
        graph = defaultdict(list)
        letters = set()
        for i in range(n):
            for j in range(m):
                letters.add(board[i][j])
                for l, k in adj:
                    if 0 <= i + l < n and 0 <= j + k < m:
                        graph[(i,j)].append((i+l,j+k))
                        
        for i in word: 
            if i not in letters: return False
            
        def bfs(i,j):
            w = board[i][j]
            p = set()
            p.add((i,j))
            Q = deque([( w, i, j, 0, p)])
            while Q:
                current, r, c, level, path = Q.popleft()
                if current == word: return True
                for l, k in graph[(r,c)]:
                    if board[l][k] == word[level+1]:
                        if (l,k) in path: continue
                        p = path.copy()
                        p.add((l,k))
                        Q.append( (current+board[l][k], l, k, level + 1, p) )
            return False
            
        for i in range(n):
            for j in range(m):
                if word[0] == board[i][j]:
                    if bfs(i,j):
                        return True
        return False




