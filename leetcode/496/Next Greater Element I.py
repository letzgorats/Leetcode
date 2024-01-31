
# monotonic stack - O(n)
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # All integers in nums1 and nums2 are unique.

        stack = []
        mapping = {}
        answer = []

        for n in nums2:
            
            while stack and n > stack[-1]:
                mapping[stack.pop()] = n

            stack.append(n)
            
        # print(stack)
        # print(mapping)
        return [mapping.get(n, -1) for n in nums1]


# brute force - O(n^2)
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # All integers in nums1 and nums2 are unique.

        answer = []
        for n in nums1:
            
            for i in range(nums2.index(n)+1,len(nums2)):

                if nums2[i] > n:
                    answer.append(nums2[i])
                    break
            else:
                answer.append(-1)
            
        return answer
            
