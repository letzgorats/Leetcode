# solution 1 - (hash table,greedy,array) - (51ms) - (2025.09.10)
from typing import List
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        known = [set() for _ in range(len(languages) + 1)]
        for person in range(1, len(languages) + 1):
            known[person] = set(languages[person - 1])

        print(known)

        # 소통불가 쌍 수집
        cannot_talk_pairs = []
        for [u, v] in friendships:
            if not (known[u] & known[v]):
                cannot_talk_pairs.append((u, v))

        # 이미 모든 친구쌍이 소통가능하면 0
        if not cannot_talk_pairs:
            return 0

        # 언어 교육 대상 후보 집합 수집
        candi = set()
        for (u, v) in cannot_talk_pairs:
            candi.add(u)
            candi.add(v)

        print(candi)

        # "한 가지 언어"를 골라서 가르칠 때, 최소인원 계산
        # "후보들 중 이미 그 언어를 아는 사람이 많을수록 새로 가르쳐야 할 인원 수가 준다."

        language_cnt = [0] * (n + 1)
        for c in candi:
            for l in known[c]:
                language_cnt[l] += 1

        max_known = 0
        for l in range(1, n + 1):
            max_known = max(max_known, language_cnt[l])

        answer = len(candi) - max_known

        return answer


# solution 2 - (array,hash table,network) - (51ms) - (2025.09.11)
from collections import defaultdict


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        cncon = set()
        for friendship in friendships:
            mp = {}
            conm = False
            for lan in languages[friendship[0] - 1]:
                mp[lan] = 1
            for lan in languages[friendship[1] - 1]:
                if lan in mp:
                    conm = True
                    break
            if not conm:
                cncon.add(friendship[0] - 1)
                cncon.add(friendship[1] - 1)

        max_cnt = 0
        cnt = [0] * (n + 1)
        for friendship in cncon:
            for lan in languages[friendship]:
                cnt[lan] += 1
                max_cnt = max(max_cnt, cnt[lan])

        return len(cncon) - max_cnt