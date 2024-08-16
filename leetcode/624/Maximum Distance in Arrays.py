# solution 1
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        min_val = 10000
        max_val = -10000

        second_min_val = 10000
        second_max_val = -10000

        min_idx, max_idx = 0, 1

        for idx, m in enumerate(arrays):

            current_min = min(m)
            current_max = max(m)

            if current_min < min_val:
                second_min_val = min_val
                min_val = current_min
                min_idx = idx

            elif current_min < second_min_val:
                second_min_val = current_min

            if current_max > max_val:
                second_max_val = max_val
                max_val = current_max
                max_idx = idx

            elif current_max > second_max_val:
                second_max_val = current_max

        if min_idx == max_idx:
            return max(second_max_val - min_val, max_val - second_min_val)
        else:
            return max_val - min_val

# solution 2 - simple code
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        cur_min, cur_max = arrays[0][0], arrays[0][-1]
        res = 0

        for arr in arrays[1:]:
            res = max(res,arr[-1]-cur_min,cur_max-arr[0])

            cur_min = min(arr[0],cur_min)
            cur_max = max(arr[-1],cur_max)


        return res