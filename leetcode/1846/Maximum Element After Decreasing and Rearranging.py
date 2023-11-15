class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        arr = sorted(arr)
        arr[0] = 1

        for idx in range(len(arr)-1):
            # arr[idx+1] = min(arr[idx]+1,arr[idx+1])
            if abs(arr[idx+1] - arr[idx]) > 1:
                arr[idx+1] = arr[idx] + 1

        return arr[-1]
