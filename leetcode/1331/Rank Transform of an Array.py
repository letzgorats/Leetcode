# solution 1
from collections import  defaultdict
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        rank = defaultdict(int)
        sorted_arr = sorted(arr)

        for idx, num in enumerate(sorted_arr):

            if len(rank) > 0:
                if sorted_arr[idx - 1] == num:
                    rank[num] = rank[sorted_arr[idx - 1]]
                else:
                    rank[num] = rank[sorted_arr[idx - 1]] + 1

            elif len(rank) == 0:
                rank[num] = idx + 1

        answer = [0] * len(arr)
        for i, a in enumerate(arr):
            answer[i] = rank[a]

        return answer


# solution 2
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        numbers = sorted(set(arr))
        rank = {}
        for i, num in enumerate(numbers):
            rank[num] = i + 1

        return [rank[num] for num in arr]