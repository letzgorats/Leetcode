'''
        good pairs
        -> nums[j]-nums[i] == j-i
        -> nums[j]-j == nums[i]-i

        전체 가능한 쌍의 개수는 -> (n-1)*n // 2
        bad pairs = 전체 쌍의 개수 - good_pairs
        '''

# solution 1
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:



        bad_pairs = 0
        diff_count = {}

        for pos in range(len(nums)):
            diff = pos - nums[pos]

            good_pairs_count = diff_count.get(diff, 0)

            bad_pairs += pos - good_pairs_count

            diff_count[diff] = good_pairs_count + 1

        return bad_pairs


# solution 2
from collections import Counter
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        n = len(nums)
        total_pairs = (n-1) * n // 2

        freq = Counter()
        good_pairs = 0

        for i,num in enumerate(nums):

            key = num - i   # nums[i] - i
            good_pairs += freq[key] # 이전에 같은 key 가 나온 횟수만큼 good_pairs 증가
            freq[key] += 1  # 현재 key 등장 횟수 업데이트

        return total_pairs - good_pairs

