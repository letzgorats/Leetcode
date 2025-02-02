class Solution:
    def check(self, nums: List[int]) -> bool:

        start = nums.index(min(nums))
        non_decreasing = nums[start:] + nums[:start]
        flag = False
        for idx in range(1, len(non_decreasing)):

            if non_decreasing[idx - 1] <= non_decreasing[idx]:
                if flag:
                    if non_decreasing[idx] > non_decreasing[0]:
                        return False
                else:
                    continue
            else:
                if non_decreasing[idx] <= non_decreasing[0]:
                    flag = True
                    continue
                else:
                    return False

        return True