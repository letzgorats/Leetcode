class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        del nums1[m:] 
        nums1.extend(nums2[:n])
        nums1.sort()

        """
        Do not return anything, modify nums1 in-place instead.
        """
