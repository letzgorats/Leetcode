# solution 1
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        a = list(map(str, s1.split()))
        b = list(map(str, s2.split()))
        removed = []

        for word in a:
            if a.count(word) > 1:
                removed.append(word)

        for word in b:
            if b.count(word) > 1:
                removed.append(word)

        common = set(a) & set(b)
        for r in removed:
            if r in a:
                a.remove(r)
            if r in b:
                b.remove(r)

        return list(set(a) - common) + list(set(b) - common)



# solution 2
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        a = list(map(str, s1.split()))
        b = list(map(str, s2.split()))

        res = []
        for i in a:
            if i not in b and a.count(i) < 2:
                res.append(i)

        for i in b:
            if i not in a and b.count(i) < 2:
                res.append(i)

        return res