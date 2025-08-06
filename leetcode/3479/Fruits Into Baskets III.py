# solution 1 - (Segment Tree, binary search) - (3109ms) - (2025.08.06)
from typing import List
import math

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        h = (self.n - 1).bit_length()
        size = 1 << (h + 1)
        self.tree = [0] * size
        self.build(data)

    def build(self, data):
        def helper(node, left, right):
            if left == right:
                self.tree[node] = data[left]
            else:
                mid = (left + right) // 2
                helper(node * 2, left, mid)
                helper(node * 2 + 1, mid + 1, right)
                self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])
        helper(1, 0, self.n - 1)

    def update(self, index, value):
        def helper(node, left, right):
            if left == right:
                self.tree[node] = value
            else:
                mid = (left + right) // 2
                if index <= mid:
                    helper(node * 2, left, mid)
                else:
                    helper(node * 2 + 1, mid + 1, right)
                self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])
        helper(1, 0, self.n - 1)

    def query(self, fruit):
        def helper(node, left, right):
            if self.tree[node] < fruit:
                return -1
            if left == right:
                return left
            mid = (left + right) // 2
            if self.tree[node * 2] >= fruit:
                return helper(node * 2, left, mid)
            else:
                return helper(node * 2 + 1, mid + 1, right)
        return helper(1, 0, self.n - 1)

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        st = SegmentTree(baskets)
        unplaced = 0

        for fruit in fruits:
            pos = st.query(fruit)  # 가장 왼쪽의 fruit 이상을 담을 수 있는 바구니 찾기
            if pos == -1:
                unplaced += 1
            else:
                st.update(pos, -1)  # 사용한 바구니는 capacity = -1로 표시

        return unplaced

'''
Segment Tree란?
 - Segment Tree 는 "배열의 구간 정보(합, 최댓값, 최솟값 등)" 를 빠르게 구하기 위한 트리 기반 자료구조이다.
 - (ex)
    arr = [3,5,1,4,2]
    이런 배열에서 "인덱스 1~3 구간의 최댓값은?" 같은 질문을 빠르게 처리하고 싶을 때 쓴다.

왜 필요한가?
 - 일반적으로 [l,r] 범위의 합/최댓값을 구할 때 O(n) 시간이 걸린다.
 - Segment Tree는 이를 O(logn) 안에 처리하게 해준다.
 -> 대규모 데이터(n<=10^5) 에서 반복되는 구간 질의가 빠르게 가능하다.

구조 요약
 - 배열 크기 n 일 때, Segment Tree 는 보통 4*n 크기의 트리 배열로 관리한다.
 - 트리는 이진트리 형태이다.
 - 각 노드는 배열의 구간 정보를 저장한다.
 - 예 : tree[1] -> 전체 [0,n-1] 범위의 최댓값
        tree[2] -> 왼쪽 절반
        tree[3] -> 오른쪽 절반 ...
- (ex) 배열 [3,5,1,4]
        tree[1] -> max(3,5,1,4) = 5
        ├── tree[2] -> max(3,5) = 5
        │   ├── tree[4] -> 3
        │   └── tree[5] -> 5
        └── tree[3] -> max(1,4) = 4
            ├── tree[6] -> 1
            └── tree[7] -> 4

| 연산               | 의미           | 시간 복잡도   |
| ---------------- | ------------ | -------- |
| `build()`        | 트리 초기 생성     | O(n)     |
| `query(l, r)`    | 구간 정보 질의     | O(log n) |
| `update(i, val)` | 값 변경 시 트리 갱신 | O(log n) |

이 문제에서는?
 - 각 fruit[i] 에 대해, 왼쪽부터 오른쪽으로 보면서
 - 아직 사용되지 않았고, basket[j] >= fruit[i] 인 가장 왼쪽 j를 찾아야 함.
이걸 Segment Tree 를 이용해서 아래처럼 해결할 수 있다.
 - 1. Segment Tree 에 baskets 를 저장(각 노드는 구간 최댓값)
 - 2. 각 fruit 에 대해, query(fruit) 을 통해
    - 가장 왼쪽에서 fruit[i] 이상인 basket 의 위치를 찾아
 - 3. 그 위치를 사용했으면 Segment Tree 에서 해당 위치를 -1로 업데이트

이해 key point
 - 1. Segment Tree는 배열을 트리 형태로 쪼개서 구간 정보를 빠르게 알 수 있게 해줌
 - 2. query()는 "이 범위에서 내가 찾는 조건을 만족하는 값이 있니?" 라고 물어보는 것.
 - 3. update()는 "이 값은 이제 못 쓰게 됐어!" 라고 알려주는 것.
 
'''