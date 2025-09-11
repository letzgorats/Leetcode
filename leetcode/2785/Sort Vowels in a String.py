# solution 1 - (greedy,string) - (183ms) - (2023.11.13)
class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        vowels = ['A','a','E','e','I','i','O','o','U','u']

        upper_seen = []
        lower_seen = []
        change_index = []
        s = list(s)

        for idx,alpha in enumerate(s):

            if alpha in vowels:
                if alpha.islower():
                    lower_seen.append(alpha)
                    change_index.append(idx)
                elif alpha.isupper():
                    upper_seen.append(alpha)
                    change_index.append(idx)

        lower_seen = sorted(lower_seen)
        upper_seen = sorted(upper_seen)

        for i in range(len(upper_seen)):
            s[change_index[i]] = upper_seen[i]
    
        change_index = change_index[len(upper_seen):]
        for i in range(len(lower_seen)):
            s[change_index[i]] = lower_seen[i]
    

        return "".join(s)


# solution 2 - (string,greedy,sort) - (75ms) - (2025.09.11)
from collections import defaultdict
class Solution:
    def sortVowels(self, s: str) -> str:

        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        temp = []
        idx = []
        ans = ['-'] * len(s)

        for i, alpha in enumerate(s):

            if alpha not in vowels:
                ans[i] = alpha
            else:
                temp.append(alpha)
                idx.append(i)

        temp.sort()
        idx.sort()

        j = 0
        for i in idx:
            ans[i] = temp[j]
            j += 1

        return "".join(ans)