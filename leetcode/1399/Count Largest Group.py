# solution 1 - string,sum - (39ms) - (2025.04.23)
class Solution:
    def countLargestGroup(self, n: int) -> int:

        # all_sum = defaultdict(list)
        len_list = [0] * (n + 1)
        for i in range(1, n + 1):
            tmp = 0
            for x in str(i):
                tmp += int(x)
            len_list[tmp] += 1
            # all_sum[tmp].append(i)

        return len_list.count(max(len_list))

# solution 2 - helper, while - (17ms) - (2025.04.23)
class Solution:
    def countLargestGroup(self, n: int) -> int:

        def digit_sum(num):
            total = 0
            while num:
                total += (num % 10)
                num //= 10
            return total

        len_list = [0] * (n + 1)
        for i in range(1, n + 1):
            len_list[digit_sum(i)] += 1

        return len_list.count(max(len_list))