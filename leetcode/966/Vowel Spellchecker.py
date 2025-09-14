# solution 1 - (set,hash table) - (31ms) - (2025.09.14)
from typing import List
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        VOWELS = set("aeiou")

        def devowel(s: str) -> str:
            # 소문자로 바꾸고, 모음은 '*'로 치환
            s = s.lower()
            res = []
            for ch in s:
                if ch in VOWELS:
                    res.append('*')
                else:
                    res.append(ch)
            return ''.join(res)

        # 1) 정확 일치용: 집합 (O(1))
        exact = set(wordlist)

        # 2) 대소문자 무시용: lower(word) -> 첫 등장 원본 단어
        lower_map = {}
        # 3) 모음 오류 무시용: devowel(lower(word)) -> 첫 등장 원본 단어
        devowel_map = {}

        # 첫 등장 우선이므로, 키가 없을 때만 채운다
        for w in wordlist:
            lw = w.lower()
            pat = devowel(w)
            if lw not in lower_map:
                lower_map[lw] = w
            if pat not in devowel_map:
                devowel_map[pat] = w

        ans = []
        for q in queries:
            if q in exact:
                # 정확 일치면 쿼리 그대로 반환 (문제 요구사항)
                ans.append(q)
                continue

            lw = q.lower()
            if lw in lower_map:
                ans.append(lower_map[lw])
                continue

            pat = devowel(q)
            if pat in devowel_map:
                ans.append(devowel_map[pat])
                continue

            ans.append("")

        return ans

# TLE
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        def vowel_error_match(w1):

            nonlocal tmp1
            t1 = list(w1.lower())
            for i, alpha in enumerate(t1):
                if alpha in {'a', 'e', 'i', 'o', 'u'}:
                    t1[i] = '*'

            for w2 in wordlist:
                t2 = list(w2.lower())
                for i, alpha in enumerate(t2):
                    if alpha in {'a', 'e', 'i', 'o', 'u'}:
                        t2[i] = '*'

                if t1 == t2:
                    tmp1 = w2
                    return True

            return False

        def capitalization(w1):
            nonlocal tmp2
            # print(w1)
            t = w1.lower()
            for w2 in wordlist:
                if t == w2.lower():
                    tmp2 = w2
                    # print(tmp2)
                    return True

            return False

        answer = []
        tmp1, tmp2 = "", ""
        for word in queries:

            if word in wordlist:
                answer.append(word)

            elif capitalization(word):
                answer.append(tmp2)

            elif vowel_error_match(word):
                answer.append(tmp1)

            else:
                answer.append("")

        return answer