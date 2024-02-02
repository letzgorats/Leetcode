class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """

        low = str(low)
        high = str(high)
        s = len(low)
        f = len(high)
        nums = '0123456789'

        answer = []
        start = low[0]

        while s <= f:
            
            for i in range(9):
                if s+(int(start)+i) > 10:
                    break 
                j = nums.index(str(int(start)+i))
                tmp = nums[j:j+s]
                if int(tmp) < int(low):
                    continue
                if int(tmp) > int(high):
                    break
                answer.append(int(tmp))

            s += 1    
            start = '1'
            
        return answer
