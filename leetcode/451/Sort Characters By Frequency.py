class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = defaultdict(int)

        for i in s:
            count[i] += 1
        
        tmp = sorted(count.items(),key = lambda x : x[1],reverse= True)
        answer = ""
        for t in tmp:
            answer += (t[0] * int(t[1]))

        return answer
