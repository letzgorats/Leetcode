# solution 1 - greedy, O(n) - (187ms) - (2025.04.03)
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        largest, diff, triplets = 0, 0, 0
        for i in range(len(nums)):
            triplets = max(diff * nums[i], triplets)
            diff = max(largest - nums[i], diff)
            largest = max(nums[i], largest)

        return triplets
'''
i < j < k를 만족하는 순서를 지키기 위해서, 계산은 과거 값을 기반으로 하고, 갱신은 나중에 해야 한다.
즉, 현재 순회하고 있는 i 를 k처럼 바라보면서(즉, 마지막 값으로 바라보면서) 가야 한다.

                       순서             |          이유
largest_triple  :   계산 먼저            |       현재 i를 k로 보고 계산
largest_diff    :    그 다음            |       i < j 를 만족하기 위해
largest_num     :    마지막에 갱신        |       i < j < k 순서 보장 위해

'''