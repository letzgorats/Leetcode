# solution 1 - math, prefix
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        n = len(arr)
        prefix, cnt = 0, 0
        for i in range(n):

            prefix += arr[i]
            # 누적합이 인덱스까지의 합(수열의 합 공식)과 같아진다면, chunk 생성 가능한지점
            if prefix == (i * (i + 1)) / 2:
                cnt += 1

        return cnt

# solution 2 - max
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        max_val, cnt = 0, 0
        for i, num in enumerate(arr):

            max_val = max(max_val, num)
            if max_val == i:  # 최대값이 인덱스와 같다면, chunk 생성 가능
                cnt += 1

        return cnt