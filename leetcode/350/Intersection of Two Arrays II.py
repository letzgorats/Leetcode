from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        hashs = {}
        standards = nums1
        if len(nums1) == min(len(nums1), len(nums2)):
            hashs = Counter(nums1)
            standards = nums2
        else:
            hashs = Counter(nums2)
            standards = nums1

        answer = []
        for i in range(len(standards)):

            if standards[i] in hashs and hashs[standards[i]] > 0:
                hashs[standards[i]] -= 1
                answer.append(standards[i])

        return answer
