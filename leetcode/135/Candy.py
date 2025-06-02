# solution 1 - (greedy) - (16ms) - (2025.06.02)
class Solution:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)
        candies = [1] * n
        # 왼쪽 -> 오른쪽 스캔
        # 앞보다 크면 + 1
        for left in range(1, n):
            if ratings[left] > ratings[left - 1]:
                candies[left] = candies[left - 1] + 1

        # 오른쪽 -> 왼쪽 스캔
        # 뒤보다 크면 뒤 애보다 + 1 또는 유지 중 큰값
        for right in range(n - 2, -1, -1):
            if ratings[right] > ratings[right + 1]:
                candies[right] = max(candies[right], candies[right + 1] + 1)

        # print(candies)

        return sum(candies)


'''
1) 왼쪽 -> 오른쪽 스캔
: 오른쪽 아이가 왼쪽보다 rating이 높다면, 오른쪽 아이는 왼쪽보다 사탕을 1개 더 받아야 한다.
: 즉, ratings[i] > ratings[i-1] -> candies[i] = candies[i-1] + 1

2) 오른쪽 -> 왼쪽 스캔
: 왼쪽 아이가 오른쪽보다 rating이 높다면, 왼쪽 아이는 오른쪽보다 사탕을 1개 더 받아야 한다.
: 그런데, 왼쪽 아이느느 이미 왼쪽->오른쪽 스캔에서 사탕을 받았을 수도 있으니까
-> max(현재값, 오른쪽+1) 을 써서, 조건을 위반하지 않으면서도 최소로 유지해야 한다.(중요 포인트!)

'''
