# TLE - difference array,prefix,binary search - (2025.05.22)
# 조합 queries 개수가 20개 이상일 때는 조합개수가 수백만개라서 TLE 가 날 수 밖에 없다.
from typing import List
from itertools import combinations

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:

        def is_valid(keep_indices):

            diff = [0] * n
            for i in keep_indices:
                l, r = queries[i]
                diff[l] -= 1
                if r + 1 < n:
                    diff[r + 1] += 1

            # 누적합 적용
            s = 0
            for i in range(n):
                s += diff[i]
                if nums[i] + s > 0:
                    return False  # 아직 0까지 도달 못하니까 바로 return False

            return True  # zero_array 만들 수 있다.

        # 이분 탐색: 제거할 수 있는 최대 개수
        n = len(nums)
        m = len(queries)
        left, right = 0, m
        answer = -1

        while left <= right:
            remove_cnt = (left + right) // 2
            keep_cnt = m - remove_cnt

            found = False
            for keep_indices in combinations(range(m), keep_cnt):
                if is_valid(keep_indices):
                    found = True
                    break

            if found:  # 더 많이 제거할 수 있는지 시도
                answer = remove_cnt
                left = remove_cnt + 1  # 더 많이 제거할 수 있나 시도
            else:
                right = remove_cnt - 1  # 제거 수를 줄여야 함

        return answer


# solution 1- difference array,prefix,binary search - (243ms) - (2025.05.22)
from typing import List
import heapq


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:

        queries.sort(key=lambda x: x[0])
        q = []
        diff = [0] * (len(nums) + 1)

        prefix_sum = 0  # 현재 index까지 누적된 감소량
        j = 0

        for i, num in enumerate(nums):

            prefix_sum += diff[i]
            while j < len(queries) and queries[j][0] == i:
                # i로 시작하는 쿼리들 중 종료점이 가장 큰 쿼리부터 뽑도록 max heap으로 넣는다.
                heapq.heappush(q, -queries[j][1])
                j += 1

            # nums[i] 를 0 으로 만들기 위해 필요한 감소가 남아 있다면,
            # 지금 사용 가능한 쿼리 중에서 가장 넓게 퍼지는 쿼리부터 사용

            # 현재 꺼낼 수 있는 가장 오른쪽 쿼리의 종료점 r(-q[0]) 이 i 이상이라는 뜻
            while prefix_sum < num and q and -q[0] >= i:
                prefix_sum += 1
                diff[-heapq.heappop(q) + 1] -= 1

            # 아무리 쿼리를 써도 nums[i] 를 0으로 못 만들면 실패
            if prefix_sum < num:
                return -1

        # q에 남은 쿼리는 결국 사용하지 않아도 되는 쿼리, 즉, 제거 가능한 쿼리 수
        return len(q)
