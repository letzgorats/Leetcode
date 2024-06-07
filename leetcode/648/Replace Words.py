class Solution(object):
    def replaceWords(self, dictionary, sentence):
      
        dictionary = sorted(dictionary,key=len)
        sentence_list = list(map(str,sentence.split()))
        answer = ""

        for word in sentence_list:
            
            for w in dictionary:

                if word.startswith(w):
                    answer += w + " "
                    break
            
            else:
                answer += word + " "

        return answer.strip()
            

