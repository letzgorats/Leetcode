# float()로 직접 계산한 solution
class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        fractions = []
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                fractions.append((float(arr[i])/arr[j],arr[i],arr[j]))

        answer = sorted(fractions)[k-1]
              
        return [answer[1],answer[2]]

# heapq solution
import heapq
class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        fractions = []
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                heapq.heappush(fractions, (float(arr[i])/arr[j], i,j))

        while k > 1:
            heapq.heappop(fractions)
            k -= 1
        
        x, i, j = heapq.heappop(fractions)
        return [arr[i],arr[j]]
