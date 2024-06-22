class Solution(object):
    def numberOfSubarrays(self, nums, k):

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1

        count = {0:1}
        current_sum = 0
        answer = 0

        for num in nums:

            current_sum += num
            if current_sum-k in count:
                answer += count[current_sum-k]
            count[current_sum] = count.get(current_sum,0) + 1

        return answer