class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        
        def make_a_list(old_list):
          
          new_list = []
          temp = 0
          cnt1 = 0
          for i in range(len(old_list)-1):
            cnt1 += 1

            if old_list[i] != old_list[i+1]:
              new_list.append((old_list[i],cnt1,temp))
              temp += 1
              cnt1 = 0
          
          new_list.append((old_list[-1],cnt1+1,temp))

          return new_list

        s_list = make_a_list(s)

        answer = 0
        for w in words:
          w_list = make_a_list(w)

          if len(s_list) != len(w_list):
            continue
            
          for idx,cur in enumerate(s_list):

            if cur[0] == w_list[idx][0]:
              if cur[1] >= 3 and cur[1] >= w_list[idx][1]:
                continue
              elif cur[1] < 3 and cur[1] == w_list[idx][1]:
                continue
              else:
                break
            else:
              break
          
          else:
            answer += 1


        return answer
