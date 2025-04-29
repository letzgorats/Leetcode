# two_pointer solution, TLE solution
from collections import Counter
class Solution(object):
    def countSubarrays(self, nums, k):

        max_num = max(nums)
        cnt = Counter(nums)
        
        if cnt[max_num] < k:
            return 0

        count = defaultdict(int)

        s_index = 0
        e_index = 0
        answer = 0 

        while s_index < len(nums) and e_index < len(nums):

            count[nums[e_index]] += 1

            if count[max_num] >= k:

                answer += len(nums) - e_index
                s_index += 1
                e_index = s_index
                count = defaultdict(int)

            else:
                e_index += 1

        return answer

# sliding window solution - correct, but 6.67%(1194ms)
from collections import Counter
class Solution(object):
    def countSubarrays(self, nums, k):

        max_num = max(nums)
        cnt = Counter(nums)

        if cnt[max_num] < k:
            return 0

        s_index = 0
        e_index = 0
        answer = 0 
        max_count = 0
        
        while s_index < len(nums) and e_index <= len(nums):

            while max_count < k and e_index < len(nums):
                tmp = 0

                if nums[e_index] == max_num:
                    max_count += 1
                
                e_index += 1
            
                if max_count >= k:
                    tmp = len(nums) - e_index + 1
                    answer += tmp

            s_index += 1
            if s_index <= len(nums) and nums[s_index-1] == max_num:
                max_count -= 1
                if e_index == len(nums):
                    return answer
            else:
                answer += tmp
            

        return answer


# effective solution(66.67%,928ms)
class Solution(object):
    def countSubarrays(self, nums, k):
      
        max_num = max(nums)
        answer = freq = i = 0

        for j in range(len(nums)):
            freq += nums[j] == max_num
            while freq >= k:
                freq -= nums[i] == max_num
                i += 1
            answer += i

        return answer


# solution 3 - (subarray,monotonic,sliding window,left,right) - (234ms) - (2025.04.29)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        max_num = max(nums)
        print(max_num)

        freq = defaultdict(int)
        left = 0
        answer = 0

        for right, num in enumerate(nums):
            freq[num] += 1
            while freq[max_num] >= k:
                answer += len(nums) - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

        return answer


