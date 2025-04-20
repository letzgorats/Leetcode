# solutiuon 1 - def binary search - (111ms) - (2024.11.13)
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        nums.sort()     # 정렬 - 어차피 개수구하기이므로 인덱스로 접근 가능

        # [a--,lower,b--,upper,c--] 구간이라 하면
        # [a--,lower,b--,upper] 구간에 해당하는 카운트에서
        # [a--] 구간을 빼는 코드이다.
        # 그래서  nums[left] + nums[right] > bound: right -= 1 이고,
        # count_pairs_lower_bound(lower-1) 처럼, lower-1 을 인자로 주는 것
        def count_pairs_lower_bound(bound):

            left, right = 0, len(nums) - 1
            cnt = 0
            while left < right :
                while left < right and nums[left] + nums[right] > bound:
                    right -= 1
                cnt += (right - left)
                left += 1

            return cnt

        return count_pairs_lower_bound(upper)- count_pairs_lower_bound(lower-1)

# solution 2 - bisect - (184ms) - (2024.11.13)
from bisect import bisect_right,bisect_left
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        answer, r_up = 0, len(nums)

        # bisect_left(정렬된 리스트,해당 숫자,lo=시작인덱스,hi=끝인덱스)
        # -> 해당 숫자 이상의 첫 인덱스
        # bisect_right(정렬된 리스트,해당 숫자,lo=시작인덱스,hi=끝인덱스)
        # -> 해당 숫자 보다 큰 첫 인덱스

        # l 은 시작인덱스이고, 적절한 끝 인덱스를 찾는 순회문이라고 보면 됨.
        # lower-num 을 하면서 num + nums[r_low] 가 lower 이상인지를 찾는 과정
        # 그러니까, lower-num을 해서, 현재 바라보고 있는 num 에 최대로 더할 수 있는
        # 인덱스를 찾는 과정임. 해당 r_low 를 찾았다면,

        # lower <= x <= upper 를 구해야 하므로
        # l인데스부터 시작해서 lower 이상인 값(lower <= nums[l] + nums[r_low])을
        # 만족하는 인덱스 r_low 를 시작 인덱스로 하고 x <= upper 를 만족하도록
        # r_up 인덱스를 구해야 함.

        # 끝으로는 r_up - r_low 를 해서 답을 구함.
        for l, num in enumerate(nums):
            r_low = bisect_left(nums, lower - num, lo=l + 1, hi=r_up)
            r_up = bisect_right(nums, upper - num, lo=r_low, hi=r_up)
            answer += r_up - r_low

        return answer

"""
Consider nums = [1, 3, 5, 7], lower = 8, and upper = 10.
# First Iteration (l=0, num=1):

# lower - num = 8 - 1 = 7, so r_low will point to the first element ≥ 7 (index 3).
# upper - num = 10 - 1 = 9, so r_up will be the first index > 9 (out of bounds in this case, so len(nums)).
# Pair count: r_up - r_low = 4 - 3 = 1
# Second Iteration (l=1, num=3):

# lower - num = 8 - 3 = 5, so r_low will point to the first element ≥ 5 (index 2).
# upper - num = 10 - 3 = 7, so r_up will point to the first element > 7 (index 4).
# Pair count: r_up - r_low = 4 - 2 = 2
"""
