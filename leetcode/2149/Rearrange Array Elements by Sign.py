class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        positive = deque([])
        negative = deque([])
        

        for n in nums:
    
            if n > 0:
                positive.append(n)
            else:
                negative.append(n)

        # print(positive)
        # print(negative)

        answer = []
        n = len(nums)
        for i in range(n):
            if i % 2 == 0:
                answer.append(positive.popleft())
            else:
                answer.append(negative.popleft())

        return answer
