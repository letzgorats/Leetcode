class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        answer = [1]


        for i in range(rowIndex):
            
            temp = [0] + answer + [0]
            answer = []
            
            for j in range(len(temp)-1):
                answer.append(temp[j]+temp[j+1])
        
        return answer
