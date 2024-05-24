class Solution(object):
    def maxScoreWords(self, words, letters, score):
        
        subsets = []

        def backtracking(index,cur_list):
            
            subsets.append(cur_list[:])

            for i in range(index,len(words)):
                backtracking(i+1,cur_list + [words[i]])

        backtracking(0,[])

        # print(subsets)

        max_point = 0
        for subs in subsets:
            point = 0
            tmp = letters[:]
            for s in subs:    
                for alpha in s:
                    if alpha not in tmp:
                        point = 0
                        break
                    else:
                        tmp.remove(alpha)
                        point += score[ord(alpha)-97] 
                max_point = max(point,max_point)
              
            # print(subs, max_point)
      
        return max_point
