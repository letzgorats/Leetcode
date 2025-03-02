# solution 1 - two pointers - (0ms) - (2025.03.02)
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        i, j = 0, 0
        answer = []

        while i < len(nums1) and j < len(nums2):

            if nums1[i][0] == nums2[j][0]:

                answer.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1

            elif nums1[i][0] < nums2[j][0]:

                answer.append([nums1[i][0], nums1[i][1]])
                i += 1

            elif nums1[i][0] > nums2[j][0]:

                answer.append([nums2[j][0], nums2[j][1]])
                j += 1

        while i < len(nums1):
            answer.append([nums1[i][0], nums1[i][1]])
            i += 1

        while j < len(nums2):
            answer.append([nums2[j][0], nums2[j][1]])
            j += 1

        # print(answer)

        return answer

# solution 2 - two pointers - (4ms) - (2025.03.02)
from collections import defaultdict
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        answer = []
        id_to_num = defaultdict(int)  # idx -> num

        for idx, num in nums1:
            id_to_num[idx] = num

        for idx, num in nums2:
            id_to_num[idx] += num

        answer = sorted(id_to_num.items(), key=lambda x: x[0])

        return answer