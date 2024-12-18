# solution 1 - two pointers
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        answer = prices[:]

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):

                if prices[i] >= prices[j]:
                    answer[i] = (prices[i] - prices[j])
                    break

        return answer

# solution 2 - monotonic stack
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        stack = []  # prices without discount
        answer = prices[:]

        for idx, price in enumerate(prices):

            while stack and prices[stack[-1]] >= price:
                answer[stack.pop()] -= price

            stack.append(idx)

        return answer
