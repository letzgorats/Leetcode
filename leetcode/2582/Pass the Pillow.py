class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """

        if time < n:
            return time + 1

        direction = time // (n - 1)
        mod = time % (n - 1)
        answer = 0
        if direction % 2 == 1:
            answer = (n - mod)
        else:
            answer = (mod + 1)

        return answer

