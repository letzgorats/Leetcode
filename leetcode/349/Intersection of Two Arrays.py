# set()
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        return set(nums1) & set(nums2)


# two pointer
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        left = 0
        right = 0
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        answer = set()
        while left < len(nums1) and right < len(nums2):

            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] > nums2[right]:
                right += 1
            else:
                answer.add(nums1[left])
                left += 1
                right += 1
            
        return list(answer)
