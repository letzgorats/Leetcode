from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        if len(s) < k:
            return False
        if len(s) == k:
            return True

        s_count = Counter(s)
        odd_cnt = 0

        for alpha, v in s_count.items():
            if v % 2 == 1:
                odd_cnt += 1
        if odd_cnt > k:
            return False

        return True

'''
1. s의 길이가 k보다 작으면 false
-> s의 문자 수가 부족하므로 k개의 문자열을 만들 수 없음. 

2. 홀수 개수의 문자가 k보다 많으면 false
-> 홀수 개수의 문자는 최소 하나의 palindrome에서 각각 중심이 되어야 하므로, k개의 palindrome을 만들 수 없음.

3. 위 두 조건을 만족하면 true
-> k개의 palindrome 문자열을 정확히 만들 수 있음.
-> 짝수 개수의 문자는 원하는 대로 분배 가능하며, 남는 홀수 개의 문자도 k개의 palindrome 내에 배치 가능하기 때문!
'''

