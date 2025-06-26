# solution 1 - (array,binary search) - (1175ms) - (2025.06.25)
from typing import List
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:

        def seperate(A):
            A1 = []
            A2 = []
            for a in A:
                if a < 0:
                    A1.append(-a)
                else:
                    A2.append(a)
            A1.reverse()    # 이진탐색용(작은값부터 보기 위해서 음수배열은 절댓값순으로 정렬되도록 함)
            return A1, A2

        nums1_negative, nums1_positive = seperate(nums1)
        nums2_negative, nums2_positive = seperate(nums2)

        # 배열 A,B 에서 뽑은 곱 중에서 a*b > m 인 경우의 수를 셈
        def numProductNoGreaterThan(A, B, m):
            count = 0
            j = len(B) - 1
            for a in A:
                while j >= 0 and a * B[j] > m:
                    j -= 1
                count += j + 1
            return count

        negCount = len(nums1_negative) * len(nums2_positive) + len(nums1_positive) * len(nums2_negative)
        sign = 1

        # k 번째 곱이 음수인지 양수인지 먼저 판단
        if k > negCount:
            k -= negCount
        else:
            k = negCount - k + 1
            sign = -1  # 음수
            nums2_negative, nums2_positive = nums2_positive, nums2_negative

        # 두 값의 절댓값의 곱의 최소~최댓값 (r은 비어있을 수도 있으므로, 그냥 무한대로 설정하고 시작)
        l, r = 0, int(1e10)
        # 이진 탐색으로 곱의 최솟값 ~ 최댓값 사이에서 "mid 이하의 곱이 k 개 이상인지를 반복 탐색
        while l < r:
            mid = (l + r) // 2
            if (numProductNoGreaterThan(nums1_negative, nums2_negative, mid) +
                    numProductNoGreaterThan(nums1_positive, nums2_positive, mid) >= k):
                r = mid # r 줄이기
            else:   # k 이하면, l 늘리기
                l = mid + 1

        # l 은 이 조건을 만족하는 가장 작은 곱
        return sign * l
