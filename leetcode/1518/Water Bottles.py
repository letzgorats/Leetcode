# solution 1 - (math,greedy) - (15ms,2ms) - (2024.07.07) , (2025.10.01)
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """

        answer = numBottles
        while numBottles >= numExchange:
            answer += (numBottles // numExchange)   # drink
            numBottles = (numBottles // numExchange + numBottles % numExchange)

        return answer


