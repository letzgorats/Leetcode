from collections import Counter
class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        arr = Counter(arr)        
        arr = sorted(arr.items(),key = lambda x : -x[1])

        element, freq = arr[-1]
        answer = len(arr)

        while arr[-1][1] <= k:

            element, freq = arr.pop()

            if freq <= k:
                k -= freq
                answer = len(arr)
            
            if len(arr) == 0:
                break
        
        return answer 
