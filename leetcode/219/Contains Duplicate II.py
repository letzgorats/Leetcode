# heapq - 5 %
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        tmp = []

        for idx,num in enumerate(nums):

            heapq.heappush(tmp,(num,idx))
        
        # print(tmp)

        num1, idx1 = heapq.heappop(tmp)
        while tmp:

            num2, idx2 = heapq.heappop(tmp)

            if num1 == num2 and abs(idx1-idx2) <= k :
                return True

            num1 , idx1 = num2, idx2
        
        return False

# dict - 90%
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        d = defaultdict(int)

        for i,v in enumerate(nums):

            if v in d and abs(d[v]-i) <= k :
                return True
            d[v] = i 

        return False
