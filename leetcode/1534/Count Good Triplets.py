# solution 1 - O(n^3) - 377ms -(2025.04.14)
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        answer = []
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a:
                        if abs(arr[j] - arr[k]) <= b:
                            if abs(arr[i] - arr[k]) <= c:
                                answer.append((i, j, k))
        print(answer)
        return len(answer)