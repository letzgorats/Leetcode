# solution 1 - () - (1902ms) - (2025.12.03)
from collections import Counter
from math import gcd
from itertools import combinations

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:

        # 조합 C(n,2) = n * (n-1) // 2
        def comb2(v: int) -> int:
            return v * (v - 1) // 2

        slopes = Counter()  # 기울기만 같은 선분 쌍
        lines = Counter()  # 같은 직선 위의 선분 쌍
        mids = Counter()  # 중점이 같은 선분 쌍
        midlines = Counter()  # (중점 + 직선)까지 같은 선분 쌍

        # 이중 for문 대신, 조합(combinations)을 써도 되고,
        # range 이중 루프를 써도 똑같이 동작함
        for (x1, y1), (x2, y2) in combinations(points, 2):
            dx = x2 - x1
            dy = y2 - y1

            # 서로 다른 점들이라 dx,dy가 동시에 0이 될 일은 없음(문제 조건)
            g = gcd(dx, dy)
            dx //= g
            dy //= g

            # 방향 정규화: (dx, dy)를 한쪽 방향으로만 통일
            #  - dx < 0 이면 둘 다 부호 반전
            #  - dx == 0이면 dy > 0 이 되도록(수직선 처리)
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy

            # 직선의 "고유값" 만들기
            # 같은 직선이면 dx * y - dy * x 값이 항상 동일함
            inter = dx * y1 - dy * x1  # line 식의 일종의 상수항

            # 선분의 중점(사실은 1/2를 안 나눠도 됨, (x1+x2, y1+y2)로만 써도 유일함)
            mid_x = x1 + x2
            mid_y = y1 + y2

            # 각각 카운터에 기록
            slopes[(dx, dy)] += 1  # 같은 기울기인 모든 선분 수
            lines[(dx, dy, inter)] += 1  # 같은 직선 위의 선분 수
            mids[(mid_x, mid_y)] += 1  # 같은 중점을 갖는 선분 수
            midlines[(mid_x, mid_y, dx, dy, inter)] += 1  # (중점+직선)까지 같은 선분 수

        # 포함-배제 원리로 trapezoid 개수 계산
        ans = 0

        # 1) 기울기만 같은 모든 선분 쌍(= 평행한 선분 쌍)에서 시작
        ans += sum(comb2(v) for v in slopes.values())

        # 2) 같은 직선 위에 있는 선분 쌍은 trapezoid를 만들 수 없으므로 빼기
        ans -= sum(comb2(v) for v in lines.values())

        # 3) 중점이 같은 선분 쌍도 사다리꼴이 안 되므로 빼기
        ans -= sum(comb2(v) for v in mids.values())

        # 4) 하지만 (중점+직선)까지 같은 경우는 위에서 두 번 뺐으니 한 번 다시 더해줌
        ans += sum(comb2(v) for v in midlines.values())

        return ans
