# solution 1 - (dp,dfs) - () - (2025.08.27)
from typing import List
class Solution:
    DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])

        # Step 1) 전처리 : run2[d][r][c], run0[d][r][c]
        # d = 0...3 for NE,SE,SW,NW
        run2 = [[[0] * m for _ in range(n)] for _ in range(4)]
        run0 = [[[0] * m for _ in range(n)] for _ in range(4)]

        def inb(r, c):
            return 0 <= r < n and 0 <= c < m

        # 각 방향 d 마다 "끝에서 시작으로" 순회 순서를 정하자.
        # -> NE(-1,+1) : r는 0...n-1 증가, .c는 m-1..0 감소가 유리(다음이 r-1,c+1)
        #   하지만 구현을 단순화 하려고 "다음 칸을 미리 계산"하는 방식으로 공통 루프로 처리하자.

        for d, (dr, dc) in enumerate(self.DIRS):

            # 모든 칸을 뒤에서 앞으로 스캔하려면, 다음 칸이 범위 안에 있을 때
            # 이미 채워졌다고 보장되는 순서로 돌리는 게 베스트지만
            # 여기서는 두 번 루프를 써도 여전히 O(nm)이므로 단순 구현해도 충분함.
            # 아래는 역방향 스캔을 위한 인덱스 범위 선택:
            r_range = range(n - 1, -1, -1) if dr == 1 else range(n)
            c_range = range(m - 1, -1, -1) if dc == 1 else range(m)

            for r in r_range:
                for c in c_range:
                    nr, nc = r + dr, c + dc
                    # run2
                    if grid[r][c] == 2:
                        nxt = run0[d][nr][nc] if inb(nr, nc) else 0
                        run2[d][r][c] = 1 + nxt
                    else:
                        run2[d][r][c] = 0

                    # run0
                    if grid[r][c] == 0:
                        nxt = run2[d][nr][nc] if inb(nr, nc) else 0
                        run0[d][r][c] = 1 + nxt
                    else:
                        run0[d][r][c] = 0

        # 여기까지가 Step 1(전처리 DP). 이 상태에서 직선형 최대(꺾지 않음)는
        # 모든 1쉘과 모든 d 에 대해 1+run2[d][next(r,c,d)] 중 최댓값으로 찾을 수 있음.
        # Step2에서는 "한 번 꺾는" 경우를 포함해서 전체 답을 계산하면 됨.

        ans = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] != 1:
                    continue

                # For each initial diagonal direction d
                for d, (dr, dc) in enumerate(self.DIRS):
                    nr, nc = r + dr, c + dc

                    # (A) straight (no turn) : must follow 2,0,2,0,...after the initial 1
                    straight = 1 + (run2[d][nr][nc] if inb(nr, nc) else 0)
                    if straight > ans:
                        ans = straight

                    # (B) V-shaped with one clockwise 90-degree turn
                    # First arm length L1 (after the initial 1) is limited by the alternating run

                    if not inb(nr, nc) or grid[nr][nc] != 2:
                        continue  # cannot even take the first step of the first arm

                    L1 = run2[d][nr][nc]  # how many cells we can go in the first arm starting with 2
                    cw = (d + 1) % 4
                    p_r, p_c = nr, nc  # pivot advances along the first arm

                    # Walk k = 1..L1 steps along first arm; at each step, try turning
                    # After k steps, next expected is:
                    #   if k is even -> 2 ; if k is odd -> 0
                    for k in range(1, L1 + 1):
                        # turn at pivot p=(p_r,p_c), then continue from q = p + DIRS[cw]
                        q_r, q_c = p_r + self.DIRS[cw][0], p_c + self.DIRS[cw][1]
                        add2 = 0
                        if inb(q_r, q_c):
                            if k % 2 == 0:
                                add2 = run2[cw][q_r][q_c]  # expect 2
                            else:
                                add2 = run0[cw][q_r][q_c]  # expect 0
                        v_len = 1 + k + add2  # 1 for the starting '1'
                        if v_len > ans:
                            ans = v_len

                        # advance pivot by one step along first arm for next k
                        if k < L1:
                            p_r += dr
                            p_c += dc

        return ans

