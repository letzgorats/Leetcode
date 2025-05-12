# solution 1 - (permutations) - (2698ms) - (2025.05.12)
from typing import List
from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        candi = set()

        for perm in permutations(digits, 3):
            # print(perm)
            if perm[0] != 0 and perm[2] % 2 == 0:
                num = perm[0] * 100 + perm[1] * 10 + perm[2]
                candi.add(num)

        return sorted(candi)


# solution 2 - (counter, all, hash table) - (55ms) - (2025.05.12)
from typing import List
from collections import Counter
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        count = Counter(digits)
        result = []

        # 100부터 999까지 모든 짝수 탐색
        for num in range(100, 1000, 2):  # 짝수만 탐색
            hunds, tens, ones = num // 100, (num // 10) % 10, num % 10

            # 현재 숫자를 구성하는 각 자리수의 개수가 충분한지 확인
            candidate = Counter([hunds, tens, ones])
            # print(candidate)
            # 모든 자릿수가 count에 충분하면 결과에 추가
            if all(candidate[digit] <= count[digit] for digit in candidate):
                result.append(num)

        return result


# TLE - backtracking
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        candi = set()

        def backtracking(cur, options):

            if len(cur) == 3:

                num = int(''.join(map(str, cur)))
                if num % 2 == 0 and cur[0] != 0:
                    candi.add(num)
                return

            for i in range(len(options)):
                curr = cur + [options[i]]
                backtracking(curr, options[:i] + options[i + 1:])

        backtracking([], digits)
        # print(candi)

        return sorted(candi)
'''
backtracking은 시간초과 
digits 길이가 최대 100까지 갈 수 있는데, 순열의 개수는 n!이므로
20! 만 해도 2,432,902,008,176,640,000 → 불가능한 수준
'''