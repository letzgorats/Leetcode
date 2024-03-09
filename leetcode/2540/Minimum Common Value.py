# two pointer solution
class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        left, right = 0, 0

        while left != len(nums1) and right !=len(nums2) :

            if nums1[left] < nums2[right]:
                left += 1

            elif nums1[left] > nums2[right]:
                right += 1
        
            else:
                return nums1[left]
        
        return -1


# set solution

class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        return min(set(nums1) & set(nums2) or [-1])
# 교집합이 있을 경우, min 함수는 교집합 집합 내의 최소값을 반환합니다. 예를 들어, 교집합이 {2, 3}이라면, min({2, 3})의 결과는 2입니다.
교집합이 없을 경우, 즉 교집합 결과가 빈 집합이라면, or [-1]에 의해 [-1] 리스트가 min 함수의 인자로 전달됩니다. 이 경우, min([-1])의 결과는 -1입니다. 리스트 내에서 최소값을 찾는 것이므로, 리스트에 단 하나의 원소만 있을 때는 그 원소가 최소값입니다.
따라서 return min(set(nums1) & set(nums2) or [-1]) 코드에서 교집합이 없으면 [-1]이 리스트 형태로 min 함수에 전달되고, min 함수는 이 리스트의 유일한 원소인 -1을 반환합니다. 결과적으로 -1이 반환됩니다, 리스트 형태가 아니라 단일 값으로 말이죠.

