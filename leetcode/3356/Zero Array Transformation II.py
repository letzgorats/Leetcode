# TLE - (623/627) - (dictionary,greedy) - (2025.03.13)
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        idx_to_val = defaultdict(int)

        for idx, num in enumerate(nums):
            if num != 0:
                idx_to_val[idx] = num

        # print(idx_to_val)
        if len(idx_to_val) == 0:
            return 0

        for k, q in enumerate(queries):

            l, r = q[0], q[1]
            val = q[2]

            for i in range(l, r + 1):
                if i in idx_to_val:
                    idx_to_val[i] -= val

                    if idx_to_val[i] <= 0:
                        del idx_to_val[i]

            if len(idx_to_val) == 0:
                return k + 1

        return -1

# solution 1 - (binary search, difference array) - (1115ms) - (2025.03.13)
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        '''
        우리가 원하는 건 k를 최소화하는 것 -> 이진탐색
        즉, `k` 값이 가능하다면 더 작은 `k` 로 시도해보고,
        불가능하면, `k` 를 늘리는 방식
        '''

        '''
        'k'개의 쿼리만 사용했을 때 배열을 0으로 만들 수 있는가? 를 빠르게 판단
        -> 각 인덱스에서 감소해야 할 총합을 구해서, `k`개의 쿼리로 충족할 수 있는지 확인
        -> `prefixs sum` 또는 `sorted list`같은 자료구조를 활용해서 범위 내 감소량을 빠르게 계산
        '''

        n = len(nums)

        def is_valid(k):
            """첫 k개의 쿼리를 사용해서 모든 원소를 0으로 만들 수 있는지 확인"""
            # 차분배열 -> i 번째 원소의 변화량을 저장하는 배열
            '''
            차분 배열에 변화를 적용할 때는
                1. 변화가 시작되는 지점에 +변화량
                2. 변화가 끝나는 지점 + 1에 -변화량
            '''
            delta = [0] * (n + 1)
            for i in range(k):
                l, r, val = queries[i]
                delta[l] -= val
                delta[r + 1] += val  # 차분 배열

            # 누적합으로 실제 배열 값 계산
            curr_val = 0
            temp_nums = nums[:]
            for i in range(n):
                curr_val += delta[i]
                temp_nums[i] += curr_val
                if temp_nums[i] > 0:  # 아직 0이 아닌 값이 있다면 실패
                    return False
            return True

        # binary search on k (0~len(queries))

        left, right = 0, len(queries)
        answer = -1

        while left <= right:

            mid = (left + right) // 2

            if is_valid(mid):
                answer = mid  # mid 가 가능하다면, 더 작은 k를 탐색
                right = mid - 1
            else:
                left = mid + 1  # mid 가 불가능하다면, 더 큰 k 탐색

        return answer

# solution 2 - (diffenence array + greedy, two poiners) - (143ms)- (2025.03.13)
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        k = cur_sum = 0
        diff_arr = [0] * (len(nums) + 1)
        q_idx = 0  # 현재 사용할 쿼리 인덱스

        for i in range(len(nums)):

            while cur_sum + diff_arr[i] < nums[i]:

                if k == len(queries):
                    return -1

                l, r, val = queries[k]
                k += 1

                if r < i:
                    continue

                diff_arr[max(l, i)] += val
                diff_arr[r + 1] -= val

            cur_sum += diff_arr[i]

        return k