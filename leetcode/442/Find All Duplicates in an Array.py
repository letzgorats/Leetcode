class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        candi = set()
        answer = []
        for n in nums:
            if n not in candi:
                candi.add(n)
            else:
                answer.append(n)
        
        return answer


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        cnt = Counter(nums)

        answer = []
        for k,v in cnt.items():

            if v == 2:
                answer.append(k)
            
        return answer
