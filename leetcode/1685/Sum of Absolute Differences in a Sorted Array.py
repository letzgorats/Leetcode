class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]

        for idx in range(1,n):
            prefix[idx] = prefix[idx-1] + nums[idx]
        # print(prefix)

        suffix = [0] * n
        suffix[-1] = nums[n-1]

        for idx in range(n-2,-1,-1):
            suffix[idx] = suffix[idx+1] + nums[idx] 
        # print(suffix)
        
        answer = [0] * n
        answer[0] = suffix[1] - nums[0] * (n-1)
        answer[-1] = (n-1) * nums[-1] - prefix[-2]

        for idx in range(1,n-1):

            temp1 = (nums[idx] * idx) - prefix[idx-1]
            temp2 = suffix[idx+1] - (nums[idx] * (n-idx-1))
            
            answer[idx] = temp1 + temp2
    

        # answer = []
        # for i in range(len(nums)):
        #     temp = 0
        #     for j in range(len(nums)):

        #         if i != j:
        #             temp += abs(nums[i]-nums[j])
        #     answer.append(temp)
        

        return answer



class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        left = 0
        right = sum(nums)
        answer = []

        for idx in range(n):

            if len(answer) == 0:
                answer.append(right-n*nums[idx])
            else:
                answer.append(nums[idx]*idx-left + right-nums[idx]-(n-idx-1)*nums[idx])
            left += nums[idx]
            right -= nums[idx]
            

        return answer
            
        
