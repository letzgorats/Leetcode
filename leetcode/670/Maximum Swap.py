# solution 1 - O(n^2)
class Solution:
    def maximumSwap(self, num: int) -> int:

        idx_hash = {}
        for idx, digit in enumerate(list(str(num))):
            idx_hash[digit] = idx

        num_list = list(str(num))
        for i in range(len(num_list)):
            for d in range(9, int(num_list[i]), -1):
                if str(d) in idx_hash and idx_hash[str(d)] > i:
                    num_list[i], num_list[idx_hash[str(d)]] = num_list[idx_hash[str(d)]], num_list[i]
                    return int(''.join(num_list))

        return num

# solution 2 - O(n)
class Solution:
    def maximumSwap(self, num: int) -> int:

        num_list = list(str(num))
        n = len(num_list)

        max_idx = n-1

        swap_i, swap_j = -1,-1

        for i in range(n-2,-1,-1):
            if num_list[i] < num_list[max_idx]:
                # 교환할 위치 업데이트
                swap_i, swap_j = i, max_idx
            elif num_list[i] > num_list[max_idx]:
                max_idx = i # 새로운 최대 숫자 발견

        if swap_i != -1:
            num_list[swap_i], num_list[swap_j] = num_list[swap_j], num_list[swap_i]

        return int(''.join(num_list))

# solution 3 - suffix : O(n)
class Solution:
    def maximumSwap(self, num: int) -> int:

        num_list = list(str(num))
        n = len(num_list)

        # suffix_max 배열 생성 : 뒤에서부터 각 위치에서의 최대값 인덱스 저장
        suffix_max_index = [0] * n
        suffix_max_index[n - 1] = n - 1

        for i in range(n - 2, -1, -1):
            if num_list[i] > num_list[suffix_max_index[i + 1]]:
                suffix_max_index[i] = i
            else:
                suffix_max_index[i] = suffix_max_index[i + 1]

        for i in range(n):

            if num_list[i] < num_list[suffix_max_index[i]]:
                num_list[i], num_list[suffix_max_index[i]] = num_list[suffix_max_index[i]], num_list[i]
                break

        return int("".join(num_list))