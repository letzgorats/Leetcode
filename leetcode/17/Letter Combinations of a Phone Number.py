class Solution(object):
    def letterCombinations(self, digits):

        answer = []

        digitToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"}

        
        def backtracking(i,curStr):

            if len(digits) == len(curStr):
                answer.append(curStr)
                return 
            
            for alphabet in digitToChar[digits[i]]:
                backtracking(i+1, curStr + alphabet)
            
        if digits:
            backtracking(0,"")
        
        return answer
