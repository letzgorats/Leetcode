class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        
        answer = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                answer[i+j].append(nums[i][j])

        # print(answer)

        result = []
        for k,v in answer.items():
            for i in v[::-1]:
                result.append(i)

        return result

        '''
        (0 0)
        (1 0) (0 1)
        (2 0) (1 1) (0 2)
        (3 0) ----------- (0 3)
        (4 0) ------------------(0 4)
        '''
