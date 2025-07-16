# solution 1 - (array,dynamic programming,heapq) - (399ms) - (2025.07.19)
from typing import List
import heapq
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:

        n = len(nums)
        k = n // 3

        part1 = [0] * (k + 1)

        # max heap
        # 왼쪽 힙 처리(가장 작은 합 A 만들기)
        ql = [-x for x in nums[:k]]
        heapq.heapify(ql)
        total = sum(nums[:k])
        part1[0] = total

        for i in range(k, k * 2):
            total += nums[i]        # 새 원소 포함
            heapq.heappush(ql, -nums[i])    # 힙에 추가
            total -= -heapq.heappop(ql)     # 가장 큰 수 하나 제거
            part1[i - (k - 1)] = total      # 누적 최소합 저장
        '''
        i 가 늘어날수록 가능한 선택 조합이 생기기 시작한다.
        즉, nums[0:i+1] 에서 n 개를 뽑았을 때 가장 작은 합이 저장된다.
        '''


        # min heap
        qr = nums[k * 2:]
        heapq.heapify(qr)
        part2 = sum(nums[k * 2:])
        ans = part1[k] - part2

        # 오른쪽 범위를 거꾸로 확장하면서, 가능한 조합 중 가장 큰 합을 유지
        for i in range(k * 2 - 1, k - 1, -1):
            part2 += nums[i]
            heapq.heappush(qr, nums[i])
            part2 -= heapq.heappop(qr)
            ans = min(ans, part1[i - k] - part2)

        return ans


'''
왼쪽에서는 가장 작은 합(A)을 만들고, 
오른쪽에서는 가장 큰 합(B)을 만들어야 한다.

그래야 A-B 가 가장 작아지므로, A는 작을수록 좋고, B는 클수록 좋다.
'''