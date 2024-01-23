class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """

        def backtracking(i,curStr):
            if i == len(arr):
                return len(curStr)
            
            # arr[index] 내의 문자가 모두 유일한지 확인
            if len(arr[i]) != len(set(arr[i])):
                return backtracking(i + 1, curStr)
            
            # 중복된 문자가 있는지 확인
            if any (ch in curStr for ch in arr[i]):
                return backtracking(i+1, curStr)

            # 현재 문자열을 추가하는 경우와 추가하지 않는 경우를 모두 고려
            return max(backtracking(i+1,curStr+arr[i]), backtracking(i+1,curStr))
        
        return backtracking(0,"")
