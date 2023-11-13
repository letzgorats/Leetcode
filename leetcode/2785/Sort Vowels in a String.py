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
