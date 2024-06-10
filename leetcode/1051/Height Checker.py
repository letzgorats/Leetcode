class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        answer = 0
        for idx,h in enumerate(sorted(heights)):

            if heights[idx] != h:
                answer += 1
        
        return answer
