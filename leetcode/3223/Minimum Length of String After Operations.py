# solution 1 - Greedy
from collections import defaultdict,Counter
class Solution:
    def minimumLength(self, s: str) -> int:

        s_cnt = Counter(s)

        if all(value < 3 for value in s_cnt.values()):
            return len(s)

        s = list(s)
        tmp_cnt = defaultdict(list)
        while any(value >= 3 for value in s_cnt.values()):
            for idx, alpha in enumerate(s):

                tmp_cnt[alpha].append(idx)
                if len(tmp_cnt[alpha]) >= 3:
                    # tmp_cnt[alpha].pop(0)
                    # tmp_cnt[alpha].pop(-1)
                    tmp_cnt[alpha] = tmp_cnt[alpha][1:-1]

            pos = sorted((v, key) for key, values in tmp_cnt.items() for v in values)
            # for key,values in tmp_cnt.items():
            #     for v in values:
            #         pos.append((v,key))

            # pos.sort()

            s = [key for _, key in pos]
            s_cnt = Counter(s)

        return len(s)


# solution 2 - count,math
class Solution:
    def minimumLength(self, s: str) -> int:

        s_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z'}

        ans = 0
        for ch in s_set:
            count = s.count(ch)
            if count & 1:  # 홀수면
                ans += 1
            elif count != 0:  # 짝수면
                ans += 2
        return ans

'''
count 가 홀수면 어차피 1개만 남는다. + 1
count 가 짝수면 어차피 2개만 남는다. + 2
'''