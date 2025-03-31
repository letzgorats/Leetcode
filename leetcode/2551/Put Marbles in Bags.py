# solution 1 - heapq, math - () - (2025.03.31)
import heapq
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        '''
        어떻게 접근할까?
        step 1)
        - 구간을 나누는 지점의 특징 관찰
        - 배열이 [w1,w2,w3,w4,....,wn] 일 때, 구간을 나누는 지점이 w2,w3,w4,....wn-1 에서 결정된다.

        step 2)
        - 나누는 지점마다 생기는 점수는
        - (w1 + wx) + (wx + wy) + .... + (wz + wn)

        - 위 형태를 다시 보면, 각 경계값이 두 번씩 더해지는 형태이다.
        - 즉, "점수 = w1 + wn + (나누는 지점의 양 옆 원소 합들의 합)"

        step 3)
        - 최대 점수를 얻기 위해서는 인접한 두 수의 합 중 가장 큰 값들을 골라야 하고,
        - 최소 점수를 얻기 위해서는 가장 작은 값들을 골라야 한다.
        - 따라서, priority queue 를 사용하여 빠르게 "가장 큰 합, 가장 작은 합" 을 구할 수 있다.

        ## 인접한 두 수의 합을 모두 구해서 배열을 만든다.
        paris = [ weights[i] + weights[i+1] for i in range(len(weights)-1)]

        (ex) weights = [1,3,5,1]

        쪼개기 가능한 경계는 어디일까?
        [1 | 3 , 5,  1] -> 경계 사이의 값들의 합 : 1 + 3 = 4
        [1 , 3 | 5,  1] -> 경계 사이의 값들의 합 : 3 + 5 = 8
        [1 , 3 , 5 | 1] -> 경계 사이의 값들의 합 : 5 + 1 = 6

        따라서, pairs = [4,8,6] 이 되어야 한다.
        4,8,6 중에 가장 큰 순서로 k 개를 더하고, 가장 작은 순서대로 k 개를 더해서 서로 빼면 답이다.
        '''

        # 인접한 두 수의 합을 모두 구해서 배열을 만듦
        pairs = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]

        # 최소 점수 : 이 배열에서 가장 작은 값 (k-1)개 선택
        # 최대 점수 : 이 배열에서 가장 큰 값 (k-1)개 선택

        # nsmallest(n,iterable) : iterable 안에 가장 작은 n개의 값을 리스트로 반환
        min_k = heapq.nsmallest(k - 1, pairs)

        # nlargest(n,iterable) : iterable 안에 가장 큰 n개의 값을 리스트로 반환
        max_k = heapq.nlargest(k - 1, pairs)

        # 차이 계산 (w1,wn 은 공통으로 더해지니 생략 가능)

        diff = sum(max_k) - sum(min_k)

        return diff