from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        # Step 1: Merge words2 into a single frequency map
        # 최대 개별 문자 빈도 찾기
        maxCharFreq = Counter()
        for w2 in words2:
            wordFreq = Counter(w2)
            for char in wordFreq:
                maxCharFreq[char] = max(maxCharFreq[char], wordFreq[char])

        # Step 2: Filter words1 based on maxCharFreq
        # words2의 maxChar을 기준으로 선별된 개별 단어가 words1의 각 단어에 대해 있는지 확인
        answer = []
        for w1 in words1:
            wordFreq = Counter(w1)
            isUniversal = True
            for char in maxCharFreq:
                # word1s 에 있는 각 개별단어 개수가 충족되지 못한다면,
                if wordFreq[char] < maxCharFreq[char]:
                    isUniversal = False
                    break
            if isUniversal:
                answer.append(w1)

        return answer


'''
# words1 = ["cccbaaa", "abccccc", "aabbcc", "abcabc", "bbbcccaaa"]
# words2 = ["abc", "cc", "bb"]

# maxCharFreq: {"a": 1, "b": 2, "c": 2}
-> 1. 각 단어의 문자를 개별적으로 빈도 계산한다.
-> 2. 각 문자의 최대 빈도를 유지하여, words2의 모든 단어가 만족해야 할 병합된 조건을 생성한다.
# answer = ["aabbcc", "abcabc", "bbbcccaaa"]
'''