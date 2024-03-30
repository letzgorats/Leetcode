from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums, k):
        def atMostKDistinct(k):
            count = defaultdict(int)  # 각 숫자의 출현 횟수를 저장하는 딕셔너리
            left = 0  # 윈도우의 왼쪽 포인터
            res = 0  # 결과값을 저장할 변수
            for right in range(len(nums)):  # 윈도우의 오른쪽 포인터를 배열의 끝까지 이동
                if count[nums[right]] == 0:  # 새로운 숫자가 추가될 때 k를 감소
                    k -= 1
                count[nums[right]] += 1  # 현재 숫자의 출현 횟수 증가
                
                while k < 0:  # k가 0보다 작아지면, 즉 윈도우에 서로 다른 숫자가 k개보다 많으면
                    count[nums[left]] -= 1  # 윈도우 왼쪽에서 숫자를 하나 제거
                    if count[nums[left]] == 0:  # 해당 숫자의 출현 횟수가 0이 되면 k를 증가
                        k += 1
                    left += 1  # 윈도우의 왼쪽 포인터 이동
                
                res += right - left + 1  # 현재 윈도우의 서로 다른 숫자가 k개 이하일 때 가능한 부분 배열의 수를 더함(right는 고정이고 left 땡기면서 가능한 조합 찾는 경우의 수)
            return res
        
        # 정확히 k개의 서로 다른 숫자를 가진 부분 배열의 수 = 최대 k개를 가진 부분 배열의 수 - 최대 k-1개를 가진 부분 배열의 수
        return atMostKDistinct(k) - atMostKDistinct(k-1)


# 부분 배열의 수 계산: 각 단계에서, res에 현재 윈도우에서 가능한 부분 배열의 수를 더합니다. 이는 right - left + 1을 통해 계산된다. 이 공식은 현재 윈도우의 길이에 해당하는 부분 배열의 수를 나타낸다.

# 정확히 k개의 서로 다른 정수를 가진 부분 배열의 수: 최종적으로, 정확히 k개의 서로 다른 정수를 가진 부분 배열의 수를 찾기 위해, atMostKDistinct(k) - atMostKDistinct(k-1)를 계산한다. 

# 여기서 atMostKDistinct(k)는 최대 k개의 서로 다른 정수를 포함할 수 있는 모든 부분 배열의 수이고, atMostKDistinct(k-1)은 최대 k-1개를 포함할 수 있는 모든 부분 배열의 수이다.

# 이 둘의 차이는 정확히 k개의 서로 다른 정수만을 포함하는 부분 배열의 수를 나타냅니다.


'''
우선, **"최대 k개의 서로 다른 정수를 포함하는 부분 배열"**이란, 부분 배열 안에 있는 서로 다른 정수의 수가 k개 이하인 모든 경우의 수를 말한다. 

예를 들어, 배열이 [1,2,1,3,4]이고 k=3이라면, [1,2,1], [2,1,3], [1,2,1,3] 등이 해당된다.
여기서는 k개 미만의 서로 다른 정수를 포함하는 경우도 포함되기 때문에, 실제로는 우리가 원하는 조건(정확히 k개의 서로 다른 정수)보다 더 많은 경우가 포함된다.


"정확히 k개의 서로 다른 정수를 포함하는 부분 배열" 은 말 그대로 부분 배열 안에 정확히 k개의 서로 다른 정수가 들어있는 모든 경우의 수이다.
이 두 개념 사이의 차이를 이해하는 것이 중요하다. 왜냐하면 우리가 원하는 것은 후자이지만, 알고리즘으로 직접 계산하기 쉬운 것은 전자이기 때문이다. 따라서 우리는 전자의 계산을 활용하여 후자를 도출한다.

계산 방법은 다음과 같다:

"최대 k개의 서로 다른 정수를 포함하는 부분 배열"의 수를 계산한다. 이는 "k개 또는 그보다 적은 서로 다른 정수"를 포함하는 모든 가능한 부분 배열의 수이다.

"최대 k-1개의 서로 다른 정수를 포함하는 부분 배열"의 수를 계산합니다. 이는 "k-1개 또는 그보다 적은 서로 다른 정수"를 포함하는 모든 가능한 부분 배열의 수이다.

두 계산 결과의 차이를 구한다. 이 차이는 정확히 k개의 서로 다른 정수를 포함하는 부분 배열만을 포함하게 된다.
왜냐하면, "최대 k개"에는 k개를 포함하는 모든 부분 배열이 포함되어 있지만, "최대 k-1개"에는 그렇지 않기 때문이다.
따라서, "최대 k개"에서 "최대 k-1개"를 빼면, 남는 것은 "정확히 k개"만을 포함하는 부분 배열의 수가 된다.

예를 들어, 배열이 [1,2,1,2,3]이고 k=2일 때, "최대 2개의 서로 다른 정수"를 포함하는 부분 배열은 [1,2], [2,1], [1,2], [2,3] 등이 있고,
"최대 1개의 서로 다른 정수"를 포함하는 부분 배열은 [1], [2], [1], [2], [3] 등이 있다. 여기서 전자에서 후자를 빼면, 정확히 2개의 서로 다른 정수만을 포함하는 부분 배열의 수를 구할 수 있게 된다.
'''

# solution
from collections import Counter

class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
      
        def atmostK(k):

            cnt = Counter()
            left = 0
            res = 0

            for right in range(len(nums)):

                if cnt[nums[right]] == 0 :
                    k -= 1
                
                cnt[nums[right]] += 1

                while k < 0 :

                    cnt[nums[left]] -= 1
                    if cnt[nums[left]] == 0 :
                        k += 1
                    left += 1
                
                res += right - left + 1

            return res

        return atmostK(k) - atmostK(k-1)



