# solution 1 - greedy, array,O(n^3) - (158ms) - (2025.04.02)
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        answer = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    answer = max(answer, (nums[i] - nums[j]) * nums[k])

        return answer

# solution 2 - greedy, O(n) - (0ms) - (2025.04.02)
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        largest_num = 0
        largest_diff = 0
        largest_triple = 0
        for i in range(len(nums)):
            largest_triple = max(largest_triple, largest_diff * nums[i])
            largest_diff = max(largest_num - nums[i], largest_diff)
            largest_num = max(largest_num, nums[i])

        return largest_triple

'''
i < j < k를 만족하는 순서를 지키기 위해서, 계산은 과거 값을 기반으로 하고, 갱신은 나중에 해야 한다.
즉, 현재 순회하고 있는 i 를 k처럼 바라보면서(즉, 마지막 값으로 바라보면서) 가야 한다.

                       순서             |          이유
largest_triple  :   계산 먼저            |       현재 i를 k로 보고 계산
largest_diff    :    그 다음            |       i < j 를 만족하기 위해
largest_num     :    마지막에 갱신        |       i < j < k 순서 보장 위해

'''