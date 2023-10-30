class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        numbers = []

        for i in arr:

            numbers.append((bin(i)[2:].count('1'),i))
        
        numbers.sort()

        answer = []

        for i in numbers:
            answer.append(i[1])
            
        return answer
