# solution 1 - fenwick tree, O(logn), segment Tree - (1172ms) - (2025.04.15)
class BIT:
    def __init__(self, size):
        self.tree = [0] * (size + 2)  # 1-indexed로 쓰기 위해 + 2

    def update(self, i, delta):  # 등장한 값을 기록
        i += 1  # 1-indexed로 변환
        while i < len(self.tree):
            self.tree[i] += delta
            i += (i & -i)  # 다음 영향 받는 노드로 이동

    def query(self, i):  # 누적 개수 세기
        i += 1  # 1-indexed로 변환
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= (i & -i)  # 이전 노드로 이동
        return res


'''
Q) i & -i가 뭔데?
A) 이건 이진수에서 i의 가장 낮은 1비트만 남긴 값이다.

(ex) i(10진수) -> 6, i(2진수) : 0110 , -i(2진수) : 1010
i & -i => 0010 : 2 가장 낮은 1비트만 남긴다.

Q) 이걸 왜 쓰는거야?
A) BIT 는 이런 구조이다.
tree[1] -> 1
tree[2] -> 1,2
tree[4] -> 1,2,3,4
tree[8] -> [1~8]

즉, 특정 i 에서 관리하는 구간은 i&-i 만큼의 크기다.
그래서 다음 영향받는 노드는 i + (i&-i) 인 셈이다.
'''

from collections import defaultdict
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        pos2 = defaultdict(int)

        for idx, num in enumerate(nums2):
            pos2[num] = idx

        transformed = [pos2[val] for val in nums1]
        # print(transformed)

        n = len(nums1)
        bit = BIT(n)
        left_smaller = [0] * n

        for i in range(n):
            val = transformed[i]
            left_smaller[i] = bit.query(val - 1) # val 보다 적은 수가 등장한 개수 구하기
            bit.update(val, 1) # val 가 나왔다는 걸 기록!

        # print(left_smaller)

        bit = BIT(n)
        right_larger = [0] * n

        for i in range(n - 1, -1, -1):
            val = transformed[i]
            # 전체 등장 수 - 나(val)보다 작거나 같은 값 개수 = 나보다 큰 값의 개수
            right_larger[i] = bit.query(n - 1) - bit.query(val)
            bit.update(val, 1) # val 가 나왔다는 걸 기록!

        # print(right_larger)

        answer = 0
        for i in range(n):
            # "나를 가운데로 둘 수 있는 good triplet 개수" = 왼쪽 작음 × 오른쪽 큼
            answer += left_smaller[i] * right_larger[i]

        return answer
        '''
        fenwich tree가 필요한 이유
        -> 배열에서 "나보다 앞에 있는 값 중 나보다 작은 값의 개수를 빠르게 알고 싶을 때"
        혹은 "나보다 뒤에 있는 값 중 큰 값의 개수를 빠르게 알고 싶을 때"
        brute force 방식은 O(n^3) 시간이라 fenwickTree를 고려해봐야 한다.

        fenwick tree가 해주는 일
        -> update(i,+1) : 어떤 값 i가 등장했단느 걸 기록함
        -> query(i) : 값 0~i 까지의 누적합을 빠르게 구함

        -> 이게 모두 O(logn) 시간에 가능하다.

        언제쓸까?
        -> 누적합/빈도 수를 빠르게 구해야 할 때
        -> 값의 등장 횟수 누적을 실시간으로 관리할 때
        -> i < j < k 와 arr[i] < arr[j] < arr[k] 같이 양방향 조건이 필요할 때

        transformed = [0, 2, 1, 4, 3]

        처음부터 왼쪽 → 오른쪽으로 보면서,
        예: i=2, transformed[i]=1

        그 전에 나온 값들 중에서,
        1보다 작은 값이 몇 개 있는가? → query(0)

        '''

