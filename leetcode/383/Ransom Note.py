# solution 1)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:


        dicts_magazine = defaultdict(int)
        dicts_Note = defaultdict(int)

        for i in magazine:
            dicts_magazine[i] += 1 
        for j in ransomNote:
            dicts_Note[j] += 1  
        
        for x in dicts_Note:

            if x not in dicts_magazine:
                return False

            if dicts_magazine[x] < dicts_Note[x]:
                return False
            
        return True

# solution 2)
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        for c in ransomNote:
            print(c)
            if c in magazine:
                if ransomNote.count(c) > magazine.count(c):
                    return False
            else:
                return False
        
        else:
            return True

        
        
