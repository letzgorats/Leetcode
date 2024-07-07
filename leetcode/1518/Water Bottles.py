class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """

        answer = numBottles
        while numBottles >= numExchange:
            answer += (numBottles // numExchange)
            numBottles = (numBottles // numExchange + numBottles % numExchange)

        return answer