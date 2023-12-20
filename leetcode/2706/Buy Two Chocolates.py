class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        return money - (prices[0] + prices[1]) if (money - (prices[0] + prices[1]) >=0) else money
