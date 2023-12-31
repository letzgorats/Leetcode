# filter(func, iteration(tuple,list)) 
class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        
        answer = -1
        for i in range(len(s)):

            tmp = filter(lambda x : s[x] == s[i], range(len(s)))
            # print(tmp)
            answer = max(answer,tmp[-1]-tmp[0])
        
        return answer-1

# dict
class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):

        answer = -1
        alpha = dict()

        for i in range(len(s)):

            if s[i] not in alpha:
                alpha[s[i]] = i
            else:
                answer = max(answer,i-alpha[s[i]]-1)
        return answer
        
