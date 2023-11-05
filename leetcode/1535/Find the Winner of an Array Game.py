class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
        consecutive_win = 0
        n = len(arr)
        consecutive_variable = arr[0]

        if k >= n:
            return max(arr)

        for i in range(1,n):

            # print(arr,consecutive_win,arr[0],k)
            if arr[i] < consecutive_variable:
                consecutive_win += 1
                # arr = [arr[0]] + arr[2:n] + [arr[1]]
                
            elif consecutive_variable < arr[i]:

                consecutive_variable = arr[i]
                consecutive_win = 1
                # arr = arr[1:n] + [arr[0]]
            if consecutive_win == k:
                break

        return consecutive_variable


# Consider Time Complexity -> 
- Let's get used to how to compare with an index-induced element approach "within" an array!
- Changing the arrangement itself is too exhausting.
- Hash, remember the access to the elements!
