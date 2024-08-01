class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # dp[n]에 전체 책장을 채울 때의 최소 높이가 저장
        for i in range(1, n + 1):
            width = 0
            height = 0
            for j in range(i - 1, -1, -1):
                width += books[j][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j][1])
                dp[i] = min(dp[i], height + dp[j])

        return dp[n]