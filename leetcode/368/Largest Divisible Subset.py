class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        nums = sorted(nums)
        n = len(nums)
        dp = [1] * n    
        parent = [-1] * n

        max_size = 0  # 최대 부분집합의 크기
        max_index = 0  # 최대 부분집합의 마지막 요소 인덱스

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_index = i

        # print(dp)
        # print(parent)
        # print(max_size)
        # print(max_index)
        # 최대 부분집합 재구성
        answer = []
        while max_index != -1:
            answer.append(nums[max_index])
            max_index = parent[max_index]


        return answer[::-1] 
