from collections import Counter
class Solution(object):
    def commonChars(self, words):
   
        
        a = Counter(words[0])

        for i in range(1,len(words)):

            a &= Counter(words[i])
           
        # print(a)
        answer = []
        # for k,v in a.items():
        #     for j in range(v):
        #         answer.append(k)
        

        # return answer

        return a.elements()
