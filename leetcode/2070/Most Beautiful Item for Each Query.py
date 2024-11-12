# solution 1 - bisect
from bisect import bisect_right
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        maxiBeauty_per_price = {}
        for price, beauty in items:

            if price not in maxiBeauty_per_price:
                maxiBeauty_per_price[price] = beauty
            else:
                maxiBeauty_per_price[price] = max(beauty, maxiBeauty_per_price[price])

        # print(maxiBeauty_per_price)
        maxiBeauty_per_price = dict(sorted(maxiBeauty_per_price.items()))
        prices = list(maxiBeauty_per_price.keys())
        beauties = list(maxiBeauty_per_price.values())

        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        # 각 가격별 누적 최대 아름다움 값 계산
        for i in range(1, len(beauties)):
            beauties[i] = max(beauties[i], beauties[i - 1])
        answer = [0] * len(queries)

        for idx, maxi_price in sorted_queries:
            # 'prices'에서 'maxi_price' 이하의 최대 아름다움을 찾기
            pos = bisect_right(prices, maxi_price) - 1
            if pos >= 0:
                answer[idx] = beauties[pos]

        return answer

# solution 2 - binary_search def
import heapq


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        maxiBeauty_per_price = {}
        for price, beauty in items:

            if price not in maxiBeauty_per_price:
                maxiBeauty_per_price[price] = beauty
            else:
                maxiBeauty_per_price[price] = max(beauty, maxiBeauty_per_price[price])

        # print(maxiBeauty_per_price)
        maxiBeauty_per_price = dict(sorted(maxiBeauty_per_price.items()))
        prices = list(maxiBeauty_per_price.keys())
        beauties = list(maxiBeauty_per_price.values())

        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        # 각 가격별 누적 최대 아름다움 값 계산
        for i in range(1, len(beauties)):
            beauties[i] = max(beauties[i], beauties[i - 1])
        answer = [0] * len(queries)

        # 이진 탐색 함수 구현 (bisect_right 기능을 직접 수행)
        def find_max_index(prices, target):
            left, right = 0, len(prices) - 1
            while left <= right:
                mid = (left + right) // 2
                if prices[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right  # target 이하의 최대 인덱스 반환

        for idx, maxi_price in sorted_queries:
            # 'prices'에서 'maxi_price' 이하의 최대 아름다움을 찾기
            pos = find_max_index(prices, maxi_price)
            if pos >= 0:
                answer[idx] = beauties[pos]

        return answer


