# solution 1 - (math,prefix) - (6454ms)  - (2025.11.15)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        n = len(s)
        # 바로 왼쪽에서 가장 가까운 0의 인덱스를 저장한 배열
        pre = [-1] * (n + 1)
        for i in range(n):
            if i == 0 or s[i - 1] == "0":
                pre[i + 1] = i
            else:
                pre[i + 1] = pre[i]

        # print(pre)

        res = 0
        for i in range(1, n + 1):
            cnt0 = 1 if s[i - 1] == "0" else 0
            j = i
            while j > 0 and cnt0 * cnt0 <= n:
                cnt1 = (i - pre[j]) - cnt0
                if cnt0 * cnt0 <= cnt1:
                    res += min(j - pre[j], cnt1 - cnt0 * cnt0 + 1)
                j = pre[j]
                cnt0 += 1

        return res