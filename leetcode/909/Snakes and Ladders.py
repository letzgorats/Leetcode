class Solution(object):
    def snakesAndLadders(self, board):

        def getCoordinates(s):
            # 1차원 인덱스를 2차원 게임판 위치로 변환
            quot, rem = divmod(s - 1, n)
            # row는 위에서부터 0이니까 n-1-quot 해줘야 함
            row = n - 1 - quot  
            # col은 짝수행인지, 홀수행인지에 따라, 
            # 왼쪽에서 오른쪽으로 증가하기도 하고, 오른쪽에서 왼쪽으로 증가하기도 함
            col = rem if row % 2 != n % 2 else n - 1 - rem
            return row, col

        n = len(board)
        visited = set()
        queue = deque([(1, 0)])  # 시작 지점과 주사위 굴림 횟수
        while queue:
            s, step = queue.popleft()
            for i in range(1, 7):
                if s + i <= n * n:
                    r, c = getCoordinates(s + i)
                    next_s = board[r][c] if board[r][c] != -1 else s + i
                    if next_s == n * n:
                        return step + 1
                    if next_s not in visited:
                        visited.add(next_s)
                        queue.append((next_s, step + 1))
        return -1  # 목적지에 도달할 수 없는 경우
