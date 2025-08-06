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
 - 
'''