# solution 1 - (hash, count, comb) - (7ms) - (2025.05.04)
from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        hash_dominoes = defaultdict(int)

        for a, b in dominoes:
            if (b, a) in hash_dominoes:
                hash_dominoes[(b, a)] += 1
            else:
                hash_dominoes[(a, b)] += 1

        cnt = 0
        for val in hash_dominoes.values():
            cnt += (val * (val - 1) // 2)

        return cnt

# solution 2 - (min,max) - (15ms) - (2025.05.04)
from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        hash_dominoes = defaultdict(int)

        for a, b in dominoes:
            k = (min(a, b), max(a, b))
            hash_dominoes[k] += 1

        # print(hash_dominoes)
        cnt = 0
        for val in hash_dominoes.values():
            cnt += (val * (val - 1) // 2)

        return cnt
'''
똑같은 코드인데, Key 값을 (작은값, 큰 값)으로 정규화하는 코드가 solution 2
'''