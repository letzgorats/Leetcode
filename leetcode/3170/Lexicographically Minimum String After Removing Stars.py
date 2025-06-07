# solution 1 - (heapq) - (733ms) - (2025.06.07)
import heapq
class Solution:
    def clearStars(self, s: str) -> str:

        n = len(s)

        removed = set()
        q = []
        for i in range(n):
            if s[i] == "*":
                c, index = heapq.heappop(q)
                index = -index
                removed.add(index)
            else:
                # i 가 아니라 -i를 더하는 이유는 * 기준으로 왼쪽으로 가까운 것을 골라야 하므로
                # 지금 순회는 0->n 으로 나아가고 있기 떄문에, -를 붙여서 다음 * 기준으로 왼쪽에 더 가까운 인덱스를 고려할 수 있게 하기 위함
                # 문자가 가장 작은 것
                # 문자가 같으면 인덱스가 가장 큰 것(즉, 오른쪽에서 가까운 것) 선택된다.
                heapq.heappush(q, (s[i], -i))
            # print(q)

        ans = []
        for i in range(n):
            # 제거해야 하는 부분은 append 안하고 진행
            if s[i] != "*" and i not in removed:
                ans.append(s[i])

        return "".join(ans)
