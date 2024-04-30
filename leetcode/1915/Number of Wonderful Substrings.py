class Solution(object):
    def wonderfulSubstrings(self, word):

        count = defaultdict(int)
        mask = 0
        count[0] = 1
        answer = 0

        for idx,w in enumerate(word):
          
            mask ^= (1 << (ord(w)-ord('a')))
            answer += count[mask]

            for i in range(10):
                answer += count[mask ^ (1 << i)]
            
            count[mask] += 1

        return answer
