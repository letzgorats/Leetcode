# TLE - iterative,dfs - TLE - (2025.04.10)
from functools import lru_cache
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        def count(x):
            x_str = str(x)
            n = len(x_str)

            @lru_cache(None)
            def dp(pos: int, tight: bool, leading_zero: bool, suffix: str):

                # 베이스 케이스 : 모든 자릿수 다 채운 경우
                if pos == n:
                    # leading zero가 아니고, suffix가 s로 끝나는지 확인
                    return int((not leading_zero) and suffix.endswith(s))

                total = 0
                # 현재 자리에서 선택 가능한 최대 숫자
                for digit in range(0, 10):

                    if digit > limit:
                        break  # limit 넘어가면 안 됨

                    if tight and digit > int(x_str[pos]):
                        continue  # tight 조건 넘으면 안 됨, 현재 자리는 반드시 x_str[pos] 이하여야 한다.

                    # 다음 tight : 현재 tight가 True인 상태에서만, digit == finish[pos] 일 때만 tight 유지
                    new_tight = tight and (digit == int(x_str[pos]))
                    # 그 외에는 tight -> False 로 전이된다.

                    # leading_zero 처리 : 0 이면 계속 leading_zero 유지
                    new_leading_zero = leading_zero and digit == 0
                    # leading_zero = True, digit = 0 일 때만 new_leading_zero = True 로 유지

                    # suffix 갱신 : 최대 s 길이만큼 유지
                    if new_leading_zero:
                        new_suffix = ""
                    else:
                        new_suffix = (suffix + str(digit))[-len(s):]

                        # suffix 는 지금까지 만든 숫자의 끝부분
                        # 여기에 새로운 digit 을 붙여서 , 오른쪽에서 len(s)(ex.s="124"라면, 3자리만큼 남기자는 뜻)
                        # (ex) s = "123" 인 경우
                        '''
                        현재 suffix       digit           suffix+digit         new_siffix([-3:])              
                           ""               1               "1"                     "1"
                           "1"              2               "12"                    "12" 
                           "12"             4               "124"                   "124" (일치)
                           "124"            3               "1243"                  "243" (불일치)
                           "243"            4               "2434"                  "434" (불일치)
                        '''

                    total += dp(pos + 1, new_tight, new_leading_zero, new_suffix)

                return total

            return dp(0, True, True, "")

        # start 부터 finish 까지 개수 계산
        return count(finish) - count(start - 1)

"""
dp(pos,tught,is_suffix_matched,leading_zero) 파라미터 자세히 분석

1. pos : 지금 채우고 있는 자릿수의 인덱스
- 숫자를 문자열처럼 왼쪽에서 오른쪽으로 한 자리씩 채운다고 생각하면 됨.
- 예를 들어, finish = 6000 이면, 총 4자리 -> pos 는 0부터 3까지 갈 수 있음
- DP 는 pos == len(finish_str) 이 되면 숫자 하나를 완성하는 꼴

2. tight : 현재까지 만든 숫자가 finish 의 prefix 와 같아야 하는지 여부
- 우리가 숫자를 만들면서, finish 보다 큰 숫자를 만들면 안 되니까, 
- 지금까지 만든 숫자가 finish 의 앞자릿수랑 정확히 같다면, 다음 자릿수도 조심해서 골라야 한다.
(ex) finish = 6471, 현재 pos = 0 으로 아직 아무것도 안 골랐다고 해보면,
- 만약 첫 자리를 6으로 고르면, tight = True 유지(finish의 첫 자리랑 같으니까)
- 첫 자리를 만약 5로 고르면, 그 이후부턴 아무 숫자나 골라도 됨(이미 6471보다 작아졌으니까)  
    그래서 tight = False 로 전이됨
- 첫 자리를 7 로 고르면, 안된다! tight = True 일 때는 x[pos] 를 넘으면 안 된다.

즉, tight 가 True 인 동안에는 매 자릿수를 finish와 비교하면서 제한을 걸어야 하고,
한 번이라도 digit < x[pos] 이면, 그 다음부턴 tight = False 로 바뀌어서 자유롭게 선택이 가능하다.

3. is_suffix_matched : 지금까지 만든 숫자의 끝부분이 접미사 s 와 일치하는지
- 숫자 하나 다 만들었을 때만 중요!
- 예를 들어, s = "21" 이면, 만든 숫자가 "521", "221", "21" 처럼 끝나야 함.
-> 숫자를 만들면서 suffix를 따로 추적하거나, 마지막에 숫자 문자열로 보고 .endswith(s) 로 해도 된다.

4. leading_zero : 지금까지 모든 자리가 0인지 여부
- 이걸 트래킹해야 "00021"같은 것도 유효하게 만들 수 있다.
- 왜냐면 문제 조건상 숫자에 leading zero가 있을 수도 있음.(단, 접미사 s는 0으로 시작하지 않음!)

정리하면,
dp(pos,tight,leading_zero,suffix_string)
-> pos : 현재 자릿수 위치
-> tight : 현재까지 만든 prefix가 finish의 prefix 와 동일한지 여부(True면 제한 있음)
-> leading_zero : 앞자리가 아직 0으로만 구성됐는지
-> suffix_string : 지금까지 만든 숫자의 끝부분을 추적(혹은 완성 후 검사)

"""



# solution 1 - cache, top-down - (11ms) - (2025.04.10)
from functools import lru_cache
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        @lru_cache
        def dp(num_str: str, pos: int, is_tight: bool) -> int:

            # 1. 자릿수 길이가 s보다 짧으면 무조건 불가능
            if len(num_str) < len(s):
                return 0

            # 2. 자릿수 길이가 s와 같으면 비교 한 번만
            if len(num_str) == len(s):
                return int(num_str >= s)

            # 3. 현재 위치에서 접미사 붙이기 시작하는 지점
            if pos == len(num_str) - len(s):
                # tight가 깨졌거나, 현재 자리부터 s까지 비교
                return int((not is_tight) or num_str[pos:] >= s)

            total = 0
            current_digit = int(num_str[pos])

            if is_tight and current_digit <= limit:
                # 현재 자리까지 tight 유지: 두 갈래
                # 1. 지금 자리보다 작은 숫자 선택 (tight 깨짐)
                # (이런 경우가 current_digit개니까 current_digit * dp(...))
                total += current_digit * dp(num_str, pos + 1, False)
                # 2. 지금 자리 숫자 그대로 선택 (tight 유지)
                total += dp(num_str, pos + 1, True)
            else:
                # tight 깨졌거나 현재 숫자가 limit보다 큼
                # (tight를 유지할 수 없으므로, 그 이후는 limit 안에서 자유롭게 골라서 경우의 수를 구함.)
                # (limit + 1)개의 선택지 * 다음 자리의 경우의 수
                total += (limit + 1) * dp(num_str, pos + 1, False)

            return total

        # finish 까지 가능한 수를 세고, start-1 까지 가능한 수를 세서, 그 둘을 빼면,
        # start~finish 범위에서 조건을 만족하는 수만 구함.
        return dp(str(finish), 0, True) - dp(str(start - 1), 0, True)

"""
dp 구조 : dp(post,tight)

1. pos : 현재 채우고 있는 자릿수의 인덱스
- 숫자를 왼쪽부터 오른쪽으로 한 자리씩 만들어 나감.
- 예 : num_str = "215" 라면, pos = 0 -> 첫번째 자릿수 '2'
- pos == len(num_str) - len(s) 이면, 남은 자릿수는 딱 접미사 s에 해당 -> 이 때, s 비교

2. tight : 지금까지 만든 숫자가 num_str 과 완전히 같으면 True
- True : 현재 자릿수는 반드시 num_str[pos] 이하만 선택 가능
- False : 앞자릿수에서 이미 num_str[pos] 보다 작은 숫자를 선택 -> 이후 자릿수는 자유롭게 선택 가능(0~limit)
(ex)
    num_str = "5721" , limit = 6
    pos = 0 -> num_str[0] = "5"
    선택할 수 있는 digit 은
        - 0~4 -> tight 깨짐
        - 5 -> tight 유지
        - 6~0 -> X (tight 유지 중인데, num_str[pos] 보다 큼 -> 불가능)

3. 종료 조건 : 
- 전체 길이 < s 의 길이 -> 접미사 s 가 들어갈 수 없음 -> return 0
- 전체 길이 == s의 길이 -> nums_str >= s 인지 단순 비교만 하면 됨 -> return int(num_str >=s)
- pos == len(num_str) - len(s) 이면 -> 접미사 비교 위치 도달
    -> tight 깨졌거나 접미사 일치하면 OK -> return int((not tight) or num_str[pos:] >=s)

4. 로직 흐름:
    - 현재 자릿수의 가능한 digit 범위 계산
        - tight == True -> digit 은 0 ~ int (num_str[pos])
        - tight == False -> digit 은 0 ~ limit
    - 각 digit 선택에 대해 재귀 호출
        - digit < current_digit -> tight 깨짐
        - digit == current_digit -> tight 유지
        - digit > current_digit -> tight 상태에선 불가능 -> 제외
    
5. 반환값
    - 가능한 모든 경로에 대해 조건 만족하는 숫자의 개수를 합산해서 리턴
    
"""

# solution 2 - bottom up, dp - (3ms) - (2025.04.10)
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def count_valid_up_to(num_str: str) -> int:
            """
            Bottom-up 방식 Digit DP 구현

            목표: 0부터 num_str까지의 숫자 중에서
            - 모든 자릿수 숫자가 limit 이하이고
            - 접미사가 s로 끝나는 숫자의 개수를 세기

            상태 정의:
            dp[i][tight]
            - i: 현재 자릿수 위치 (왼쪽에서 오른쪽으로 탐색)
            - tight = 1: 현재까지 num_str과 동일한 prefix를 유지 중
            - tight = 0: 이미 num_str보다 작은 수가 만들어졌음 (자유롭게 digit 선택 가능)

            특별 조건:
            - 마지막 접미사 비교 시점은 pos == len(num_str) - len(s)
            """

            length = len(num_str)
            suffix_len = len(s)

            # 숫자 길이가 접미사보다 짧으면 만들 수 없음
            if length < suffix_len:
                return 0

            # 숫자 길이 == 접미사 길이면 직접 비교
            if length == suffix_len:
                return int(num_str >= s)

            # DP 테이블 초기화
            # dp[pos][tight] → 해당 위치(pos)에서 tight 상태로 만들 수 있는 유효한 숫자의 개수
            dp = [[0, 0] for _ in range(length - suffix_len + 1)]

            # 마지막 위치에서: 접미사 비교
            dp[-1][0] = 1  # tight가 깨진 경우: 어떤 접미사든 붙일 수 있음
            if num_str[-suffix_len:] >= s:
                dp[-1][1] = 1  # tight 유지 상태에서 접미사 조건을 만족하는 경우

            # 역방향으로 DP 테이블 채우기
            for i in range(len(dp) - 2, -1, -1):
                current_digit = int(num_str[i])

                # tight 유지 가능한 경우
                if current_digit <= limit:
                    # 1. digit < current_digit → tight 깨짐
                    #    → 가능한 digit 수 = current_digit
                    # 2. digit == current_digit → tight 유지
                    dp[i][1] = (
                            current_digit * dp[i + 1][0] +
                            dp[i + 1][1]
                    )
                else:
                    # tight를 유지할 수 없음 → digit은 limit까지만 선택 가능
                    dp[i][1] = (limit + 1) * dp[i + 1][0]

                # tight가 깨진 상태면 항상 0~limit까지 자유롭게 선택 가능
                dp[i][0] = (limit + 1) * dp[i + 1][0]

            return dp[0][1]  # 첫 자리에서 tight 유지 상태로 가능한 숫자 수 리턴

        # 전체 결과 = finish까지 가능한 개수 - (start-1)까지 가능한 개수
        return count_valid_up_to(str(finish)) - count_valid_up_to(str(start - 1))
