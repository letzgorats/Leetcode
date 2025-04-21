# solution 1 - prefix,min,max - (162ms) - (2025.04.21)
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = 0
        min_val, max_val = 0, 0

        for d in differences:
            prefix += d

            min_val = min(min_val, prefix)
            max_val = max(max_val, prefix)

        # 가능한 arr[0] 의 범위는 :
        # lower <= arr[0] + min_val
        # upper >= arr[0] + max_val
        # arr[0] ∈ [lower-min_val, upper-max_val]

        return max(0, (upper - max_val) - (lower - min_val) + 1)


'''
(ex) differences = [2,-1,3]
lower = 1, upper = 10

arr ->
arr[1] = arr[0] + 2
arr[2] = arr[1] - 1 = arr[0] + 1
arr[3] = arr[2] + 3 = arr[0] + 4

따라서, arr = [arr[0], arr[0] + 2, arr[0] + 1, arr[0] + 4]

모든 값이 lower <= arr[i] <= upper 를 만족해야 하니까

1 <= arr[0] <= 10
1 <= arr[0] + 2 <= 10
1 <= arr[0] + 1 <= 10
1 <= arr[0] + 4 <= 10

arr[0] 식으로 바꾸면,

1  <= arr[0] <= 10
-1 <= arr[0] <= 8
0  <= arr[0] <= 9
-3 <= arr[0] <= 6

의 교집합을 구하면 된다.

전체 가능한 범위 = intersection([
    [1,10],
    [-1,8],
    [0,9],
    [-3,6]
])
=> 최종 가능한 범위, [1,6] => 가능한 arr[0] 값 : 1,2,3,4,5,6
정답 = 6
'''

# solution 2 - prefix, min, max - (236ms) - (2025.04.21)
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:

        prefix = [0] * (len(differences) + 1)

        for i in range(1, len(differences) + 1):
            prefix[i] = prefix[i - 1] + differences[i - 1]
        # print(prefix)

        min_val = float("-inf")
        max_val = float('inf')
        for p in prefix:
            min_val = max(lower - p, min_val)
            max_val = min(upper - p, max_val)

        # print(min_val,max_val)

        return max_val - min_val + 1 if max_val >= min_val else 0

        # 가능한 arr[0] 의 범위는 :
        # lower <= arr[0] + min_val
        # upper >= arr[0] + max_val
        # arr[0] ∈ [lower-min_val, upper-max_val]

        # return max(0, (upper-max_val) - (lower-min_val)+1)


'''
(ex) differences = [2,-1,3]
lower = 1, upper = 10

arr ->
arr[1] = arr[0] + 2
arr[2] = arr[1] - 1 = arr[0] + 1
arr[3] = arr[2] + 3 = arr[0] + 4

따라서, arr = [arr[0], arr[0] + 2, arr[0] + 1, arr[0] + 4]

모든 값이 lower <= arr[i] <= upper 를 만족해야 하니까

1 <= arr[0] <= 10
1 <= arr[0] + 2 <= 10
1 <= arr[0] + 1 <= 10
1 <= arr[0] + 4 <= 10

arr[0] 식으로 바꾸면,

1  <= arr[0] <= 10
-1 <= arr[0] <= 8
0  <= arr[0] <= 9
-3 <= arr[0] <= 6

의 교집합을 구하면 된다.

전체 가능한 범위 = intersection([
    [1,10],
    [-1,8],
    [0,9],
    [-3,6]
])
=> 최종 가능한 범위, [1,6] => 가능한 arr[0] 값 : 1,2,3,4,5,6
정답 = 6
'''

# wrong solution - binary search
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:

        answer = 0
        n = len(differences)
        possible = defaultdict(list)
        df_lower = lower
        df_upper = upper

        def is_valid(first_element):

            hidden = [0] * (n + 1)
            hidden[0] = first_element

            for i in range(1, n + 1):
                hidden[i] = hidden[i - 1] + differences[i - 1]

            # print(hidden)

            if all(df_lower <= i <= df_upper for i in hidden):
                return True

            return False

        while lower <= upper:

            mid = (lower + upper) // 2
            # print(lower,mid,upper)

            if is_valid(mid):
                answer += 1
                lower = mid + 1
            else:
                upper = mid - 1

        return answer

'''
binary serach 로는 못푼다.
-> 정답은 연속된 범위의 개수이다.
-> 근데, 이진탐색은 보통 단조 증가/감소 조건이 있을 때 쓴다.
-> 여기선 prefix_sum 전체에 대해 arr[0] 범위를 제한해야 하는 문제이다.
-> 전형적인 수학적 구간 교집합 문제로 푸는게 맞다.
'''