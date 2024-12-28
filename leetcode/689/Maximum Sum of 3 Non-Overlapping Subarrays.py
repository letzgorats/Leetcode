# TLE
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:

        max_sum, res = 0, []

        def backtracking(i, chosen):

            if len(chosen) == 3 or i >= len(nums) - 1:
                nonlocal max_sum, res
                cur_sum = 0
                for j in chosen:
                    cur_sum += sum(nums[j:j + k])
                if cur_sum > max_sum:
                    max_sum = cur_sum
                    res = chosen[::]

                return

                # choose i
            chosen.append(i)
            backtracking(i + k, chosen)
            chosen.pop()

            # skip i
            backtracking(i + 1, chosen)

        backtracking(0, [])

        return res

# solution 1 - sliding window,prefix
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        # step 1 : compute the sum of all k-length subarrays
        sums = [0] * (n-k+1)
        window_sum = sum(nums[:k])
        sums[0] = window_sum

        for i in range(1,n-k+1):
            window_sum += nums[i+k-1] - nums[i-1]
            sums[i] = window_sum

        # step 2 : compute left and right max indices
        left = [0] * len(sums)
        right = [0] * len(sums)
        max_left = 0

        for i in range(len(sums)):
            if sums[i] > sums[max_left]:
                max_left = i
            left[i] = max_left
        # print(left)

        max_right = len(sums)-1
        for i in range(len(sums)-1,-1,-1):
            if sums[i] >= sums[max_right]:
                max_right = i
            right[i] = max_right
        # print(right)

        # step 3 : Find the best middle index
        max_sum = 0
        result = [-1,-1,-1]
        for mid in range(k,len(sums)-k):
            l,r = left[mid-k], right[mid+k]
            total = sums[l] + sums[mid] + sums[r]
            if total > max_sum:
                max_sum = total
                result = [l,mid,r]

        return result

# solution 2 - sliding window,dp
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:

        # processing
        k_sums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            k_sums.append(k_sums[-1] + nums[i] - nums[i - k])

        dp = {}

        def get_max_sum(i, cnt):

            if cnt == 3 or i > len(nums) - k:
                return 0

            if (i, cnt) in dp:
                return dp[(i, cnt)]

            # include
            include = k_sums[i] + get_max_sum(i + k, cnt + 1)

            # skip
            skip = get_max_sum(i + 1, cnt)
            dp[(i, cnt)] = max(include, skip)

            return dp[(i, cnt)]

        def get_indices():
            i = 0
            indices = []

            while i <= len(nums) - k and len(indices) < 3:
                include = k_sums[i] + get_max_sum(i + k, len(indices) + 1)
                skip = get_max_sum(i + 1, len(indices))

                if include >= skip:
                    indices.append(i)
                    i += k
                else:
                    i += 1

            return indices

        return get_indices()