# solution 1 - (math,combinations) - (1102ms) - (2025.06.01)
from math import comb


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:

        cnt = 0
        for a in range(min(n + 1, limit + 1)):  # a<=limit
            target = n - a  # b+c = target
            # b = 0~target, c = target-b
            # 이 때, c도 target 이하이므로 조건 만족
            # 가능한 쌍은 (0,target),(1,target-1),...,(target,0)
            # 총 target + 1 개
            if target <= limit:  # case1
                cnt += target + 1
                # b+c = target 인데, b,c <= limit 이므로 일부 조합만 가능
            # 최소값 b가 target-limit, 최댓값 b가 limit
            # 가능한 조합 수는 limit-(target-limit) + 1 = 2*limit-target+1
            elif target - limit <= limit:  # case2
                cnt += 2 * limit - target + 1
                # cnt += max(0,2*limit-target+1)

        return cnt


'''
세 아이에게 (a, b, c)로 사탕을 주는데
a + b + c = n
단, 각 a, b, c ≤ limit
이걸 다음처럼 바꿨다.

먼저 a를 0부터 min(n, limit)까지 고정한다.
그러면 b + c = n - a 가 됨.
b와 c 둘 다 0 이상 limit 이하일 때 b + c = target 되는 조합 개수는?

(for a in range(n+1) 이나 for a in range(limit+1) 로 안하는 이유는
n+1 로 하면 답은 나오겠지만, 불필요할 떄(limit가 너무 클때)도 순회를 하니까 비효율적 X
limit+1 로 하면, n이 limit 보다 작은 입력값에서는 X )

# case 1 - 둘 다 limit 이하이므로 전부 가능
target = n - a ->  b+c = target
b = 0~target, c = target-b
이 때, c도 target 이하이므로 조건 만족
가능한 쌍은 (0,target),(1,target-1),...,(target,0)
총 target + 1 개

# case 2 - 범위 내에서만 가능한 b, c 조합 필터링
(ex) limit = 2, target = 3 이라면, b+c = 3 인데, b도 c도 2보다 클수 없으므로, 가능한 쌍은
(1,2),(2,1) 이다. (0,3)이나 (3,0)이 안 된다.
즉, b는 최대 limit, 최소 target-limit 까지 가능하다.

즉, 가능한 조합 수는 limit - (target-limit) + 1 = 2*limit - target + 1 개이다.
단, target = 4-0=4, limit = 1 일떄,
cnt += 2*1-4+1 = -1 이 된다.
즉, case2에서 가능한 조합수가 음수가 될 수 있기 때문에, max(0,조합 수)로 처리해줘야 한다.
이걸 해주지 말고, 사전에 예방하고 싶다면, 단순 else가 아니라 elif limit >= target-limit 으로 걸러주면 된다.
'''