class Solution(object):
    def wordBreak(self, s, wordDict):
      
        
        def backtracking(idx,curStr):

            if idx == len(s):
                tmp.append(" ".join(curStr))
                return
            
            for until in range(idx+1,len(s)+1):

                now = s[idx:until]
                if now in wordDict:
                    backtracking(until, curStr + [now])


        wordDict = set(wordDict)
        tmp = []
        backtracking(0,[])
    
        # print(tmp)
        return tmp
