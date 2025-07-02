# solution 1 - (dp,top down,sliding window,dp) - (2768ms) - (2025.07.02)
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:

        MOD = 10 ** 9 + 7
        n = len(word)

        # 1)그룹 분할(Consecutive Groups)
        cnt = 1
        groups = []
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                cnt += 1
            else:
                groups.append(cnt)
                cnt = 1
        groups.append(cnt)
        # print(groups)

        # 2) total combinations
        total = 1
        for num in groups:
            total = (total * num) % MOD
        print(total)

        # 이미 그룹 수보다 길이가 작거나 같으므로, 예외 없이 직접 가능한 케이스이며,
        # 바로 total 반환
        if k <= len(groups):
            return total

        # 3) dp 를 통한 유효 문자열 카운트
        # k > 그룹사이즈 인 경우, 잘라진(original 보다 짧아진) 문자열 조합 수를 뺴줘야 한다.
        '''
        - dp[j] : 현재까지 처리한 그룹을 사용해 길이 j 짜리 문자열을 만드는 방식의 수
        - 슬라이딩 윈도우를 활용해 prefix sum 최적화(dp+group <= j)

        최종적으로 유효하지 않은 문자열(길이<k)의 총 수를 invalid = sum(dp) 로 계산하고,
        (total-invalid+MOD) % MOD 를 반환하면 된다.
        '''
        dp = [0] * k
        dp[0] = 1  # 아무것도 선택하지 않은 방법도 1가지

        for num in groups:
            new_dp = [0] * k
            sum_val = 0
            for s in range(k):
                if s > 0:
                    sum_val = (sum_val + dp[s - 1]) % MOD
                if s > num:
                    sum_val = (sum_val - dp[s - num - 1] + MOD) % MOD
                new_dp[s] = sum_val
            dp = new_dp

        invalid = sum(dp[len(groups):k]) % MOD

        return (total - invalid + MOD) % MOD
