# solution 1 - greedy, simultaion - (50ms) - (2025.03.03)
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        left = []
        med = []
        right = []

        for idx, num in enumerate(nums):
            if num < pivot :
                left.append(num)
            elif num == pivot:
                med.append(pivot)
            else:
                right.append(num)

        return left + med + right