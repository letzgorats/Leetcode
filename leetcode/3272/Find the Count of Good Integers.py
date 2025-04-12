# solution 1 - (product,factorial,math,hahs table, frozen set,combinations) - (2990) - (2025.0412)
from itertools import product
from math import factorial

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:

        multiset = set()

        half = (n + 1) // 2
        # print(product(range(10),repeat=half))
        for digits in product(range(10), repeat=half):

            if digits[0] == 0:  # leading zero
                continue

            if n % 2 == 0:  # 길이가 짝수라면
                full = digits + digits[::-1]
            else:  # 길이가 홀수라면
                full = digits + digits[:-1][::-1]

            num = int(''.join(map(str, full)))
            if num % k == 0:
                multiset.add(num)

                # print(multiset)

        def count_permutations(counter):
            total = sum(counter.values())  # 전체 자릿수
            numerator = factorial(total)  # n ! (분모))
            # 중복되는 조합을 나눠서 제외하는 것이 바로 factorial의 목적
            denominator = 1
            for v in counter.values():  # 각 숫자의 빈도에 대해
                denominator *= factorial(v)  # f_i ! (분자)
            return numerator // denominator  # 중복을 나눠줌

        def count_valid_permutations(counter):
            total = 0
            for d in range(1, 10):  # 첫 자리는 1~9만 가능 (0제외)
                str_d = str(d)
                if counter[str_d] == 0:
                    continue  # 해당 숫자가 없으면 넘어감
                counter[str_d] -= 1  # 앞자리에 썼다고 가정하고 개수 줄임
                total += count_permutations(counter)  # 나머지 숫자로 가능한 순열 수 계산
                counter[str_d] += 1  # 원래대로 복구
            return total

        unique_digit_counters = set()
        for num in multiset:
            counter = Counter(str(num))
            unique_digit_counters.add(frozenset(counter.items()))

        # print(unique_digit_counters)

        total_good = 0
        for frozen in unique_digit_counters:
            counter = Counter(dict(frozen))  # 다시 Counter로 변환
            if '0' not in counter:
                total_good += count_permutations(counter)
            else:
                total_good += count_valid_permutations(counter)

        return total_good


'''
'1','2','2' 이 있으면, '122','212','221' 이 가능하다.
개수는 3!/2! 으로 6/2 = 3 개가 된다.

이처럼 중복되는 조합을 나눠서 제외하기 위해 factorial 이 필요하다

'''