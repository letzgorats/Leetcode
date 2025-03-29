# solution 1 - (deque, monotonic stack,number theory,math) - (7700ms) - (2025.03.29)
from collections import deque
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        # prime score 는 해당 숫자가 가지고 있는 소인수 "개수"
        # 1은 prime score 가 0 이다. (1은 소수가 아니니까)

        # 19 는 1*19 인데, 소인수는 19이고 prime score는 1 이다.
        # 12 는 2^2*3 인데, 소인수는 2,3 이고, prime score는 2이다.

        # 소수인지 판별하는 함수
        is_prime = [True] * (max(nums) + 1)
        is_prime[0], is_prime[1] = False, False

        for i in range(2, int(sqrt(max(nums) + 1)) + 1):
            if is_prime[i]:
                for j in range(i * i, max(nums) + 1, i):
                    # 한개라도 나누어 떨어지는 수가 있다면, 그 수는 소수가 아님.
                    is_prime[j] = False

        # print(is_prime)

        def prime_score(x):
            s = set()
            for p in range(2, int(sqrt(x)) + 1):
                # p 가 소수이고 x가 p라는 소인수로 나누어 떨어진다면, p 는 x 의 소인수
                if is_prime[p] and x % p == 0:
                    s.add(p)
                    # x 가 p로 나눠지는 동안 계속 나눠서 그 소수를 완전히 제거
                    while x % p == 0:
                        x //= p

            # 위 반복문이 끝난 뒤에도 x가 1보다 크면, 남은 x는 그 자체로 소수이므로
            if x > 1:
                s.add(x)  # 마지막 소인수로서 추가 (ex.x = 97이면 루프에 안 걸리므로 여기서 필터링해줘야함)

            return len(s)

        prime_score_list = [0] * len(nums)
        for i, num in enumerate(nums):
            prime_score_list[i] = prime_score(num)

        # print(prime_score_list)

        '''
        1.
        각 숫자가 몇 개의 subarray에서 중심값이 될 수 있는지를 파악해야 한다.
        이 때 중심값이라는 것은 -> 해당 nums[i]가 해당 구간 안에서 prime score 가 가장 높은 값이라는 뜻

        2.
        이걸 위해서는
        nums[i] 보다 작거나 prime score 를 가진 값이 
        어디까지 왼쪽/오른쪽에 연속되어 있는지를 계산해야 한다.

        즉, 스택을 이용해서
        left[i] : i 를 포함해서 왼쪽으로 몇개의 요소가 있는지
        right[i] : i를 포함해서 오른쪽으로 몇개의 요소가 있는지

        이 두 값을 곱하면, nums[i] 가 중심값이 되는 subarray 개수가 된다.

        3. 왜 스택?
        스택을 사용하면 O(n) 으로 위 구간을 구할 수 있다.
        prime_score_list 에서 strictly greater 인 값을 기준으로 왼쪽/오른쪽을 자르려고 한다.
        '''

        # left : 이전에 자신보다 높은 prime_score 를 가진 값이 나오기 전까지 얼마나 연속되는지
        # -> 즉, 현재 인덱스 "i" 가 중심이 될 수 있는 subarray에서 왼쪽으로 얼마나 확장 가능한지

        left = [1] * len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and prime_score_list[stack[-1]] < prime_score_list[i]:
                stack.pop()
            if stack:
                left[i] = i - stack[-1]
            else:
                left[i] = i + 1
            stack.append(i)

        # print(left)

        # right : 다음에 자신보다 높은 prime_score 가 나올 때 까지 얼마나 갈 수 있는지
        # -> 즉, 오른쪽으로 얼마나 확장 가능한지
        right = [1] * len(nums)
        stack = []
        for i in range(len(nums) - 1, -1, -1):

            while stack and prime_score_list[stack[-1]] <= prime_score_list[i]:
                stack.pop()

            if stack:
                right[i] = stack[-1] - i
            else:
                right[i] = len(nums) - i

            stack.append(i)

        # print(right)

        # 최종적으로 중심값이 되는 서브어레이 개수
        '''
        (ex) 중심값이 nums[i] 인 서브어레이들
        = (왼쪽으로 확장된 것 * 오른쪽으로 확장된 것) 만큼 서브어레이를 가질 수 있다.
        '''
        count = 1
        nums_count = []
        for i in range(len(nums)):
            count = left[i] * right[i]
            nums_count.append((nums[i], i, count))

        nums_count = deque(sorted(nums_count, key=lambda x: (-x[0], x[1])))
        # print(nums_count)

        answer = 1
        mod = 10 ** 9 + 7
        while k > 0:
            num, idx, count = nums_count.popleft()
            times = min(k, count)
            answer *= pow(num, times, mod)
            k -= times

        return answer % mod

# '''
# 1. 소수 판별: 에라토스테네스의 체 사용 ✅
# 2. 각 수의 prime score 계산 ✅
# 3. monotonic stack으로 left, right 범위 구하기 ✅
# 4. 중심값이 될 수 있는 subarray 수 = left[i] * right[i] ✅
# 5. 값을 기준으로 내림차순, 인덱스는 오름차순 정렬 → 조건에 완벽히 부합 ✅
# 6. 가장 큰 수부터 score에 곱해가며 k회 연산 수행 ✅
# '''

# solution 2 - (heapq, monotonic stack,number theory,math) - (3570ms) - (2025.03.29)
from heapq import heapify, heappop
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        N = len(nums)
        mod = 10 ** 9 + 7
        res = 1

        prime_scores = []
        for n in nums:
            score = 0
            # 51
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0:
                    score += 1
                    while n % f == 0:
                        n //= f
            if n >= 2:
                score += 1
            prime_scores.append(score)

            # print(prime_scores)
        [1,0,2,1]
        left_bound = [-1] * N
        right_bound = [N] * N

        stack = []  # indexes of decreasing or equal order scores
        '''
        이름  	      실제 탐색 방향	    의미하는 확장 방향	    확장 가능한 구간 길이
        left_bound	    왼쪽	              왼쪽으로 확장	       i - left_bound[i]
        right_bound	    오른쪽	          오른쪽으로 확장	   right_bound[i] - i
        
        => left_bound와 right_bound는 탐색은 반대 방향이지만,
            결과적으로는 해당 인덱스 기준으로 확장 가능한 서브어레이의 범위를 계산하는 데 사용되는 "경계값"이다.
        (ex) nums : [6,4,5,10,30]
             prime_score : [2,1,1,2,3]
             
             left 에서
             각 위치는 '(인덱스-1)'을 뜻한다. 즉 left[1] = 0 이니까 왼쪽으로 확장 가능한데, 현재 인덱스가 1이니까 
             (1-1)=0 이 해당 위치에 온 것이다.(주의할 점 : 같으면 어차피 왼쪽 인덱스에 있는 것이니까 확장 불가로 세팅하는 것이다!)
             (ex) prime_score[2] = 1 이지만, left[2] = 1 이 된다. 이유는 prime_score 에서 
             1번째 인덱스에 있는 prime_score[1] = 1 이니까 어차피 이걸 선택하니까, left 에서는 굳이 같은 값을 가지는 
             prime_score 인덱스까지 확장하면 안된다.
             left : [-1,0,1,0,-1]
             
             
             right 에서 
             각 위치는 '(인덱스+1)'를 뜻한다. 즉, right[0] = 4 이니까 오른쪽으로 확장 가능한데, 3번째 인덱스까지 가능해서
             (3+1)= 4가 해당 위치에 온 것이다.
             left : []
             right : [4,3,3,4,5]
        
        '''

        for i, s in enumerate(prime_scores):

            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                index = stack.pop()
                right_bound[index] = i
            if stack:
                left_bound[i] = stack[-1]
            stack.append(i)

        min_heap = [(-n, i) for i, n in enumerate(nums)]  # num, index
        heapify(min_heap)

        while k > 0:
            n, index = heappop(min_heap)
            n = -n
            score = prime_scores[index]

            left_cnt = index - left_bound[index]
            right_cnt = right_bound[index] - index

            count = left_cnt * right_cnt
            operations = min(count, k)
            res = (res * pow(n, operations, mod)) % mod

            k -= operations

        return res


''' solution 1 과의 차이점 왜 더 빨라졌을까?
1. primes_socres 직접 계산(여기서 많이 줄인 듯 하다)
- 각 n에 대해서만 소인수 분해 → O(sqrt(n)) 이내로 충분히 빠름
- (특히 max(nums)가 클 때 더 효율적)

2. 스택을 이용한 left_bound, right_bound 한 번에 계산(여기서 많이 줄인 듯 하다)
- 이전에는 Left,right 범위를 두 개의 스택 루프로 따로 계산했다.
- solution2 에서는 한 번의 스택 순회에서 left_bound, right_bound 를 동시에 처리하고 있다.
- 중간에 prime_scores[stack[-1]] < prime_scores[i] 조건이 만족되면 -> right_bound 바로 설정
- 이후 stack이 비지 않았다면 left_bound[i] 도 바로 설정
- O(n)으로 모든 범위 정보 계산 완료. 메모리에도 이득

=> left_bound와 right_bound는 탐색은 반대 방향이지만,
   결과적으로는 해당 인덱스를 중심값으로 하는 서브어레이의 확장 가능한 범위를 계산하는 데 사용되는 "경계값"이다.

(ex) nums : [6,4,5,10,30]
     prime_score : [2,1,1,2,3]

⟡ left_bound 설명
- 각 인덱스 `i`에 대해, `left[i]`는 prime_score가 "strictly greater"한 값이 왼쪽에 처음 등장한 위치.
- 따라서 `i - left[i]` 만큼 왼쪽으로 확장 가능하다.
- 예: left[2] = 1 → index 2는 index 1까지 확장 가능하다는 의미 (즉, [1,2]).

(주의: prime_score가 같은 경우는 확장 범위에 포함되지 않는다.  
같은 값은 중심값이 될 수 있기 때문에 ‘경쟁자’가 되므로 제외됨.)

⟡ right_bound 설명
- `right[i]`는 오른쪽에서 prime_score가 **strictly greater**한 값이 처음 나오는 위치.
- 따라서 `right[i] - i` 만큼 오른쪽으로 확장 가능하다.
- 예: right[0] = 4 → index 0은 index 3까지 확장 가능하다는 의미 (즉, [0,1,2,3]).

최종 확장 가능한 서브어레이 개수는:  
    `(i - left[i]) * (right[i] - i)`


3. heapq 사용
- nums 를 최댓값 기준으로 정렬하려면 일반 정렬은 O(nlogn), 하지만, heapq는 첫번째 원소만 꺼내니까 꺼낼때마다 O(logn) 이다.
- (메모리 캐시에도 더 유리)

4. pow() mod 동시에 처리하여 오버플로우 방지
'''