# sort 사용 안하고 풀어야 함.

# 최대 힙 사용
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        max_heap = []
        for n in nums:
            heapq.heappush(max_heap, -n)  # 최대 힙 사용

        for i in range(k):
            largest = heapq.heappop(max_heap)

        return -largest


# 최소 힙 사용 - 힙의 크기 k 로 유지
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        min_heap = []

        for n in nums:
            heapq.heappush(min_heap, n)
            # 힙의 크기를 k로 유지
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # 힙의 루트 요소 반환
        return heapq.heappop(min_heap)
