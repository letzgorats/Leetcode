class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        maxSum = nums[0]

        maxSumQueue = deque()

        for i in range(len(nums)):

            # print(maxSumQueue)
            if maxSumQueue:
                nums[i] += maxSumQueue[0]
            else:
                nums[i] += 0
            # print(nums)
            maxSum = max(nums[i], maxSum)
            

            while maxSumQueue and nums[i] > maxSumQueue[-1]:

                maxSumQueue.pop()

            if nums[i] > 0 :

                maxSumQueue.append(nums[i])
            
            if i >= k and maxSumQueue and maxSumQueue[0] == nums[i-k]:

                maxSumQueue.popleft()

        return maxSum
