class Solution(object):
    def checkSubarraySum(self, nums, k):

        n = len(nums)

        prefix_sum_mod_k = {0:-1}
        prefix_sum = 0

        for i in range(n):

            prefix_sum += nums[i]
            mod_value = prefix_sum % k

            if mod_value in prefix_sum_mod_k:

                if i-prefix_sum_mod_k[mod_value] > 1:
                    return True
            
            else:
                prefix_sum_mod_k[mod_value] = i
        
        return False
        
