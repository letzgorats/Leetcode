# solution 1 - (difference array,optimization,l,r) - (136ms) - (2025.05.20)
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        # 차분 배열
        '''
        x 를 더해주는 경우 (x를 빼주는 거라면, arr[l] += (-x) 이니까 arr[l] -= x, arr[r+1] += x 가 되면 된다.)
        arr[l] += x
        arr[r+1] -= x
        그러헤 만들어진 arr 의 prefix 가 최종 배열이 된다.
        '''

        n = len(nums)
        arr = [0] * n
        for idx, qry in enumerate(queries):

            l = qry[0]
            r = qry[1]
            if 0 <= l < n:
                arr[l] -= 1
            if 0 <= r + 1 < n:
                arr[r + 1] += 1

        for i in range(1, n):
            arr[i] += arr[i - 1]

        for i in range(n):
            nums[i] += arr[i]
            if nums[i] <= 0:    # 음수면 Ok
                continue
            else:   # 양수면 0을 못 만드는 것이므로 바로 False 리턴
                return False

        return True

'''
<차분 배열(difference array)의 원리> - 저번에도 다뤘지만 제대로 원리를 파악해보자!!

차분 배열은 어떤 배열 nums 가 있을 때, 
각 구간 [l,r] 의 모든 값에 동일한 값(x)를 더하거나 빼는 연산을 효율적으로 처리하고자 할 때 사용된다.

핵심 아이디어는 
arr = [0] * n 을 설정하고,
arr[l] += x, arr[r+1] -= x 를 하고, 
prefix sum 을 하면, [l,r] 구간에 x 가 누적된다는 점이다.

* 왜 이런 원리가 적용되는 걸까?

차분 배열 arr 는 값의 변화량만 저장하는 배열이다.
arr[0] = nums[0]
arr[i] = arr[i] - arr[i-1] (for i >= 1)

이걸 반대로 이용해서, 구간 [l,r]에 +x를 누적하겠다는 의도면,
arr[l] += x
arr[r+1] -= x
이렇게 바꾸고, 마지막에 누적합(Prefix_sum)을 하면 원래 배열을 복원하면서 누적 변화량이 포함된 결과가 나온다.

생각해보자, [l,r] 구간이 있는데, 
arr[l] 구간에 +x 를 하고, arr[r+1] 에 -x 를 하면,
나중에 누적합을 적용했을 때, [l:r+1] 구간에만 x가 적용된다는 걸 생각할 수 있다.
(ex) 
[1,3]에 +5(x) 라고 하면
arr[1] += 5, arr[4] -= 5 -> arr = [0,5,0,0,-5]
이걸 "누적 합"해보면, -> arr = [0,5,5,5,0] 이런식으로 [1:4] 구간에만 5 가 들어간 것을 확인할 수 있다.
이런 원리로 누적합의 결과는 즉, 전체 배열에서의 x를 더해주고 빼주고의 변화량을 의미하고 이를 각 위치(인덱스)에 맞게
원본배열값과 더해주면, 해당 배열이 원본배열에서 애초에 x를 적용해준 것과 같은 결과가 나오는 셈이다.


* 그리디 vs 차분배열+누적합 * 

<그리디>
시간복잡도 : 쿼리 개수를 Q, 배열 길이를 N 이라고 할 때, 최악의 경우, O(Q*N) -> 쿼리의 수에 따라 시간초과 가능성
<차분배열 + 누적합>
시간복잡도 : 각 쿼리당 O(1), 누적합 계산 O(N), 최종 결과 배열 계산, O(Q+N) -> 쿼리가 많을수록 효율적, 구간 업데이트에 매우 유리하다.


순서

# 1. diff 배열 구성
for l, r in queries:
    diff[l] += x
    diff[r+1] -= x

# 2. 누적합을 구해서 실제 변화량 적용(prefix sum 적용)
for i in range(1, n):
    diff[i] += diff[i-1]

# 3. 원본 배열과 합침
for i in range(n):
    nums[i] += diff[i]


'''