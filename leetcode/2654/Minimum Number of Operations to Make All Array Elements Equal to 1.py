# solution 1 - (number theory,subarray,math) - () - (2025.11.12)
import math
import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        n = len(nums)

        g = nums[0]
        # 전체 gcd 확인
        for x in nums:
            g = math.gcd(g, x)

        if g != 1:
            return -1

        # 이미 1이 존재하는 경우
        initial = nums.count(1)
        if initial:
            return n - initial

        # 최소 길이 구간의 gcd==1 찾기
        min_len = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break  # 더 짧은 건 불가능하므로 break

        # min_len-1 의 연산으로 1을 만들 수 있고
        # 이후 남은 n-1 개의 원소를 1로 만드는 데 n-1 번이 더 필요하다.
        return (n - 1) + (min_len - 1)


'''
1을 만드는 데 필요한 횟수 = (min_len - 1)
1을 전부 퍼뜨리는 데 필요한 횟수 = (n - 1)

-> 총합 = (min_len - 1) + (n - 1) = n + min_len - 2
'''
