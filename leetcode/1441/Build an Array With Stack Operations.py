class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """

        stack = []

        num = 1 
        idx = 0 

        while idx <= len(target)-1:

            if num == target[idx]:
                stack.append("Push")
                idx += 1
                num += 1

            else:
                stack.append("Push")
                stack.append("Pop")
                num += 1

        return stack
