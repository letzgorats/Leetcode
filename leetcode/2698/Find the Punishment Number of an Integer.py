# solution 1 - backtracking, brute force(1209ms)
class Solution:
    def punishmentNumber(self, n: int) -> int:

        def backtracking(idx, cur_sum, target, num_string):

            if idx == len(num_string) and cur_sum == target:
                return True

            for j in range(idx, len(num_string)):
                part = int(num_string[idx:j+1])
                if backtracking(j + 1, cur_sum + part, target, num_string):
                    return True

            return False

        ans = 0
        for i in range(1, n + 1):
            if backtracking(0, 0, i, str(i * i)):
                ans += (i * i)

        return ans

# solution 2 - math (233ms)
'''
9의 성질을 이용한 Casting Out Nines 검산법(9의 검산법)
- 수학적으로 숫자의 자릿수 합이 9로 나눈 나머지와 동일한 성질을 가진다는 원리
(ex) 1296 = (36)^2 → 1 + 2 + 9+ 6 = 18 → 1 + 8 = 9 → 1296 % 9 == 0
(ex) 2025 = (45)^2 → 2 + 0 + 2 + 5 = 9 → 2025 % 9 == 0
즉, 어떤 수 num 이 특정 조건을 만족하려면, num 과 num^2 의 자릿수 합이 같은 성질을 가져야 한다는 것.

모든 수 num 에 대해 
(num % 9) ^ 2 = num % 9 를 만족해야 한다.
→ num^2 % 9 = num % 9
이를 만족하는 num 은 오직 0,1 뿐이다.

즉, (num%9==0) or (num%9 == 1) 을 만족하지 않는 num 은 아예 고려할 필요가 없는 셈이다!

(ex) n = 20 이라면, 1부터 20까지 %9 의 값을 보면,
1 → 1
2 → 2
3 → 3
4 → 4
5 → 5
6 → 6
7 → 7
8 → 8
9 → 0
10 → 1
11 → 2
12 → 3
13 → 4
14 → 5
15 → 6
16 → 7
17 → 8
18 → 0
19 → 1
20 → 2

여기서 num%9 == 0 또는 num%9 == 1 인 숫자만 보면, 9,10,18,19 이다.

이러한 조건들을 활용하면 원래 O(nlogn) 또는 O(n 2^d) 에 가까운 탐색을 약 1/4~1/9 수준으로 줄일 수 있다!
단순한 완전탐색을 하기 전에 num%9 == 0 또는 num%9 == 1 조건을 만족하는 숫자만 따로 필터링하면 훨씬
더 빠르게 문제를 해결할 수 있다.
'''
class Solution:
    def punishmentNumber(self, n: int) -> int:

        def can_partition(num_str, target, idx, cur_sum):

            if idx == len(num_str):
                return cur_sum == target

            for j in range(idx, len(num_str)):
                part = int(num_str[idx:j + 1])
                if can_partition(num_str, target, j + 1, cur_sum + part):
                    return True

            return False

        def is_valid(i):
            return can_partition(str(i * i), i, 0, 0)

        answer = 0
        for i in range(1, n + 1):

            if i % 9 != 0 and i % 9 != 1:
                continue
            if is_valid(i):
                answer += i * i

        return answer