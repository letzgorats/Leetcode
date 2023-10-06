class Solution(object):
    def majorityElement(self, nums):

        n = len(nums)
        bar = n / 3

        count = defaultdict(int)
        
        for i in nums:
            count[i] += 1
        
        answer = []
        for k,v in count.items():
            if v > bar:
                answer.append(k)

        return answer
