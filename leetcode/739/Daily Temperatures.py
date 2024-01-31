class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        stack = []
        n = len(temperatures)
        answer = [0] * n
        
        for i in range(n):
        
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                answer[j] = (i-j)

            stack.append(i)
        # print(answer)
        return answer
