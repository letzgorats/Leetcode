class Solution(object):
    def findSpecialInteger(self, arr):
      
        n = len(arr)
        
        also = n // 4 

        for i in range(n):
            if arr[i] == arr[i+also]:
                return arr[i]
        else:
            return arr[0] 
