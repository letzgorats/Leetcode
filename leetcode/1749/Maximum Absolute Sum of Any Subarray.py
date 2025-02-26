# solution 1 - prefix_sum,brute_force - (83ms) - 2025.02.26
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur = 0
        pre_min = 0  # 현재까지 누적 합이 가장 작았던 값 (이전 구간의 최소값)
        pre_max = 0  # 현재까지 누적 합이 가장 컸던 값 (이전 구간의 최대값)
        res = 0

        for n in nums:
            pre_min = min(pre_min, cur)
            pre_max = max(pre_max, cur)

            cur += n

            # 최대 부분합을 찾으려면, 현재까지의 누적 합 cur에서
            # 최소/최대 누적 합을 빼는 것이 유리

            res = max(abs(cur - pre_min), abs(cur - pre_max), res)

        return res

    '''
    "cur-pre_min" 은 최대 증가량을 찾는 역할을 한다.
    즉, cur(현재 누적합) 에서 가장 작은 누적합(pre_min)을 빼면,
    결국 어떤 구간에서 가장 많이 증가한 값을 찾을 수 있다.
    -> 최대 양수 부분 배열의 합을 찾는 것과 동일

    "cur-pre_max" 은 최대 감소량을 찾는 역할을 한다.
    즉, cur(현재 누적합) 에서 가장 큰 누적합(pre_max)을 빼면,
    결국 어떤 구간에서 가장 많이 감소한 값을 찾을 수 있다.
    -> 최대 음수 부분 배열의 합을 찾는 것과 동일
    '''

    '''
    Kadane's Algorithm(카데인 알고리즘) 을 변형한 형태라고 할 수 있다.
    class Solution:
        def maxAbsoluteSum(self, nums: List[int]) -> int:
            max_sum, min_sum, cur_max, cur_min = 0, 0, 0, 0

            for n in nums:
                cur_max = max(cur_max + n, n)
                cur_min = min(cur_min + n, n)

                max_sum = max(max_sum, cur_max)
                min_sum = min(min_sum, cur_min)

            return max(max_sum, abs(min_sum))

    카데인 알고리즘은 "최대 부분합"과 "최소 부분합"을 각각 따로 계산하는 방법이다.
    '''

# solutino 2 - kadane's alogrithm - (93ms) - (2025.02.26)
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum, min_sum, cur_max, cur_min = 0, 0, 0, 0

        for n in nums:
            cur_max = max(cur_max + n, n)
            cur_min = min(cur_min + n, n)

            max_sum = max(max_sum, cur_max)
            min_sum = min(min_sum, cur_min)

        # print(max_sum,min_sum)
        return max(max_sum, abs(min_sum))
