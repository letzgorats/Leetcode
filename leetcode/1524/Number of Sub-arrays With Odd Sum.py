# solution 1 - prefix_sum, index - (79ms) - (2025.02.25)
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        '''
        sum(arr[i:j]) = prefix_sum[j] - prefix_sum[i-1]
        이 값이 홀수인지 확인하고 count 를 갱신하는것이 우리의 목표

        예를 들어, 현재 누적합이 6이야.(현재까지 누적합 prefix_sum[j] = 짝수인 경우)
        이 떄, "부분 배열의 합이 홀수"가 되는 경우를 찾고 싶은 것이므로,

        어떤 'prefix_sum[i-1]' 을 빼면 홀수가 될까? 를 고민해야 한다.

        즉, 이전 누적합 중에서 '홀수'였던 경우를 빼야한다.((짝수-홀수 = 홀수) 이므로)
        따라서, 이전에 홀수 였던 개수(odd_count) 만큼 count를 증가시켜줘야 한다!

        왜 odd_count 를 더할까?
        odd_count 는 이전까지 등장한 "홀수 누적합의 개수" 이다.
        현재 prefix_sum 이 짝수라면, 홀수 + 홀수 = 짝수(현재)가 되어야 하니까
        이전까지 누적합 중에서 홀수였던 것들을 빼야 "홀수 합"이 나옴!

        그럼 반대로, prefix_sum 이 현재까지 홀수라면,
        even_count 를 더해주는 이유는 even_count 가 "짝수 누적합의 개수"이니까,
        짝수 + 홀수 = 홀수(현재) 이므로,
        이전까지 등장한 "짝수 누적합(even_count) 개수만큼 부분배열을 만들 수 있기 때문"이다!

        우리는 현재 값(arr[i])이 짝수인지 홀수인지 신경 쓰는 게 아님.
        현재 prefix_sum이 짝수인지 홀수인지를 기준으로,
        "이전 누적합" 중 어떤 것들을 빼야 홀수가 되는지를 따지는 것!

        즉, 현재 숫자(arr[i])가 짝수인지 홀수인지 신경 쓰지 않고,
        이전까지의 누적합(prefix_sum[i-1])이 홀수였던 경우를 찾아야 함!

        '''

        mod = 10 ** 9 + 7
        odd_count = 0  # 홀수 prefix_sum 개수
        even_count = 1  # 초기값 (0이 하나 존재한다고 가정)
        prefix_sum = 0
        count = 0

        for num in arr:
            prefix_sum += num  # 누적 합 계산

            # 짝수 누적 합이 나올 때마다, 기존에 나온 홀수 누적 합 개수(odd_count)를 결과에 더한다.
            # prefix_sum[j]이 짝수일 때,
            # odd_count 개수를 정답에 추가하는 이유는 (홀수 - 짝수 = 홀수)이기 때문.

            # 홀수 누적 합이 나올 때마다,
            # 기존에 나온 짝수 누적 합 개수(even_count)를 결과에 더한다.
            # (짝수 - 홀수 = 홀수)

            if prefix_sum % 2 == 1:  # 누적합이 홀수라면
                count += even_count  # 이전 짝수개수만큼 추가
                odd_count += 1  # 현재 홀수 개수 증가
            else:  # 누적합이 짝수라면
                count += odd_count  # 이전 홀수 개수만큼 추가
                even_count += 1  # 현재 짝수 개수 증가

            count %= mod

        return count

        '''
        ✔ 현재까지의 누적합이 짝수라면 (prefix_sum % 2 == 0)
        ➡ 우리가 구하는 것은 홀수 합을 이루는 subArray들의 개수
        ➡ 짝수 - 홀수 = 홀수라는 특성을 이용해서
        ➡ 이전까지 나왔던 "홀수 누적합 개수 (odd_count)"를 더한다!

        ✔ 현재까지의 누적합이 홀수라면 (prefix_sum % 2 == 1)
        ➡ 우리가 구하는 것은 홀수 합을 이루는 subArray들의 개수
        ➡ 홀수 - 짝수 = 홀수라는 특성을 이용해서
        ➡ 이전까지 나왔던 "짝수 누적합 개수 (even_count)"를 더한다!
        '''

# solution 2 - dp - (104ms) - (2025.02.25)
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        N = len(arr)
        MOD = 10 ** 9 + 7
        # dp0[i]: i에서 시작하는 substring 중 합이 짝수인 것의 개수
        # dp1[i]: i에서 시작하는 substring 중 합이 홀수인 것의 개수
        dp0, dp1 = [0] * N, [0] * N

        # 초기값 설정: 마지막 원소를 기준으로 설정
        if arr[N - 1] % 2 == 0:
            dp0[N - 1] = 1
        else:
            dp1[N - 1] = 1

        for i in range(N - 2, -1, -1):  # 거꾸로 순회 - 바텀업
            if arr[i] % 2 == 0:  # 현재값이 짝수라면
                # 부분 배열의 누적합의 짝/홀 상태가 그대로 유지된다.
                dp0[i] = dp0[i + 1] + 1  # 짝수 개수는 그대로 유지하면서 1 증가
                dp1[i] = dp1[i + 1]  # 홀수 개수는 변하지 않음
            else:  # 현재 값이 홀수라면
                # 부분 배열의 누적합의 짝/홀 상태가 "반대"로 바뀐다!
                dp0[i] = dp1[i + 1]  # 짝수 개수는 기존 홀수 개수와 동일
                dp1[i] = dp0[i + 1] + 1  # 홀수 개수는 기존 짝수 개수 +1

        # print(dp1)
        # print(dp0)
        return sum(dp1) % MOD  # 합이 홀수인 모든 경우의 수 합산