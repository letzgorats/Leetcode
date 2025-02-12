# solution 1 - heapq + defaultdict (906ms)
import heapq
from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def calculate_num(number):
            val = 0
            while number > 0:
                val += (number % 10)
                number //= 10
            return val

        queue = []

        for i in range(len(nums)):
            digit_sum_num = calculate_num(nums[i])
            heapq.heappush(queue, (-nums[i], digit_sum_num))

        candi = defaultdict(list)
        # print(queue)
        max_ans = -1
        for i in range(len(queue)):

            val, digit_sum_num = heapq.heappop(queue)
            # print(-val,digit_sum_num)
            candi[digit_sum_num].append(-val)
            if len(candi[digit_sum_num]) >= 3:
                candi[digit_sum_num].remove(-val)
                if sum(candi[digit_sum_num]) < (-val + max(candi[digit_sum_num])):
                    candi[digit_sum_num].remove(min(candi[digit_sum_num]))
                    candi[digit_sum_num].append(-val)
            if len(candi[digit_sum_num]) == 2:
                max_ans = max(max_ans, sum(candi[digit_sum_num]))

            # print(candi,max_ans)

        return max_ans

# solution 2 - defaultdict(584ms)
class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def calculate_num(number):
            return sum(int(d) for d in str(number))

        candi = defaultdict(list)
        max_ans = -1

        for num in nums:

            digit_sum_num = calculate_num(num)

            candi[digit_sum_num].append(num)
            if len(candi[digit_sum_num]) > 2:
                # 현재 digit_sum_num 에 해당하는 두 개의 최댓값만 유지
                candi[digit_sum_num].remove(min(candi[digit_sum_num]))

        # 최댓값 갱신
        for values in candi.values():
            if len(values) == 2:
                max_ans = max(max_ans, sum(values))

        return max_ans
