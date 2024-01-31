class StockSpanner(object):

    def __init__(self):

        self.prices = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        stack = self.prices
        span = 1

        while stack and stack[-1][0] <= price:

            span += stack[-1][1]
            stack.pop()
        
        stack.append((price,span))
  
        return span
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
