# solution 1 - two pointers
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        i,j= 0,0
        while i < len(str1):
            while i < len(str1) and j < len(str2) and (str1[i] == str2[j] or ((ord(str1[i])+1) % 26) == (ord(str2[j]) % 26)):
                i += 1
                j += 1
            i += 1

        if j != len(str2):
            return False
        return True

# solution 2 - two pointers
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        j = 0
        for i in range(len(str1)):
            if j < len(str2) and (ord(str2[j])-ord(str1[i])) % 26 < 2:
                j += 1

        return j == len(str2)
