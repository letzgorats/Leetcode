# solution 1 - prefix
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        ans = [0] * len(queries)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefix = [0] * (len(words) + 1)

        if words[0][0] in vowels and words[0][-1] in vowels:
            prefix[1] = 1

        for idx, w in enumerate(words[1:], 2):

            if w[0] in vowels and w[-1] in vowels:
                prefix[idx] = prefix[idx - 1] + 1
            else:
                prefix[idx] = prefix[idx - 1]

        for idx, (l, r) in enumerate(queries):
            ans[idx] = prefix[r + 1] - prefix[l]

        return ans

# solution 2 - more concise version
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        ans = [0] * len(queries)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefix = [0] * (len(words) + 1)

        for idx, w in enumerate(words, 1):

            if w[0] in vowels and w[-1] in vowels:
                prefix[idx] = prefix[idx - 1] + 1
            else:
                prefix[idx] = prefix[idx - 1]

        for idx, (l, r) in enumerate(queries):
            ans[idx] = prefix[r + 1] - prefix[l]

        return ans

# TLE - wrong
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        ans = [0] * len(queries)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        v_counts = [0] * len(words)
        for idx, w in enumerate(words):

            if w[0] in vowels and w[-1] in vowels:
                v_counts[idx] += 1
            else:
                continue

        for idx, (l, r) in enumerate(queries):
            ans[idx] = sum(v_counts[l:r + 1])

        return ans