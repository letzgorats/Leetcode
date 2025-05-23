# solution  1 - array,tree,bit manipulation,xor,sorting - (32ms) - (2025.05.23)
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:

        delta = [(n ^ k) - n for n in nums]  # hard part
        delta.sort(reverse=True)

        # print(delta)

        res = sum(nums)

        for i in range(0, len(nums), 2):

            if i == len(nums) - 1:
                break
            if delta[i] + delta[i + 1] > 0:
                res += delta[i] + delta[i + 1]
            if res <= 0:
                break  # 이후 값들도 더 작을 테니 종료

        return res

'''
xor 의 특성과 트리 구조를 관찰하여 문제를 간단한 수학 문제로 변환한 셈이다.
(실질적으로는 가장 이득이 되는 노드 2개씩 짝지어서 XOR할지 말지 결정하는 문제로 단순화)
'''


'''
1. xor 연산을 같은 값으로 두 번 하면 원래 값으로 돌아온다.

→ 이건 `xor의 수학적 성질` 이다. (`x ^ k ^ k = x` 이다.)

즉, x 라는 값을 k 로 xor 하면, 어떤 중간값이 나오고, 그 값을 다시 k 로 xor 하면, 다시 원래 값인 x 로 돌아온다. 

→ 한 번 xor 하면 변경되고!

→ 두 번 xor 하면 다시 원래 값!

이 성질로 인해, 문제에서 노드 하나의 상태는 “변경”하거나 “유지”하는 두 가지 상태만 가질 수 있다는 뜻이다.

1. 아무 두 노드를 선택해 xor 할 수 있다 → 왜 그래도 되는가?

→ 원래 문제는 이렇게 주어졌다.
: `간선을 선택하면, 해당 간선에 연결된 두 노드를 둘 다 k 로 xor 해야 한다`  라고 말이다.

즉, edges = [[0,1],…] 에서 간선 0,1 을 선택하면, node 0 과 node 1 을 둘 다 xor 하는 셈이다.

그런데 중요한 관찰은

`xor을 짝수 번 하면 변화 없고, 홀수 번 하면 한 번 xor 한 것과 같다` 는 점이다.

```python
nums = [1, 2, 1]
k = 3
edges = [[0,1],[0,2]]
```

```python
    0
   / \
  1   2
```

에서 만약 [0,1] 을 선택한다면, 

0번 노드 : 1 -> 1 ^ 3 = 2

1번 노드 :  2 -> 2 ^ 3 = 1

현재 nums = [2,1,1] 로 변경된 상태

이제 또 간선 [0,2] 를 선택한다면?

0번 노드 : 2 -> 2 ^ 3 = 1 (한번 더 선택됨 → 원래값으로 복원됨)

2번 노드 :  1 -> 1 ^ 3 = 2

nums = [1,1,2]  가 됐다.

그럼 왜 “아무 두 노드를 xor 할 수 있다고 생각하면 된다” 는 걸까?

→ `xor 연산을 할 수 있는 최소 단위는 "두 노드" 이고, 어떤 두 노드를 xor 하더라도 총합의 변화를 계산할 수 있다는 의미다.` 

그래프 구조상 모든 노드는 연결되어 있으니까, 

- 간선을 여러 번 조합해서 (문제에서 같은 간선을 여러 번 선택해도 된다고 했다.)
- 임의의 두 노드만 xor 된 결과를 만들 수 있다.

이걸 이용하면,

- 어떤 노드를 xor 할지 조합을 자유롭게 구성할 수 있게 된다.
- 그 결과, 실질적으로 “아무 두 노드를 골라 xor한 것처럼 계산할 수 있다” 는 것이다.




그래서 delta 그리디가 가능하다.

- 각 노드의 xor 후 delta를 보고,
- 가장 이득이 큰 두 노드를 선택해 xor 하는 걸 반복한다.
- 실제 구현은 경로로 만들어야 하지만, 탐욕적으로 delta 쌍을 고르는 것만으로 충분한 결과를 낼 수 있다.

```python
delta.sort(reverse=True)
total = sum(nums)
for i in range(0, len(delta) - 1, 2):
    if delta[i] + delta[i + 1] > 0:
        total += delta[i] + delta[i + 1]
    else:
        break
```

`delta` 는 각 노드를 xor 했을 때 증가하는 값(이득) → `val ^ k - val`

`delta[i]` 는 i 번째 노드를 xor 했을 때 변화량

`total` 은 현재 노드들의 총합



왜 `delta.sort(reverse=True)`?

→ 이득이 큰 노드부터 먼저 고르기 위해서이다.

- xor 은 반드시 두 개의 노드를 한 쌍으로 바꿔야 한다.
- 그렇다면 이왕이면 이득이 가장 큰 두개를 쌍으로 묶는게 좋다.
- 그래서 delta 를 내림차순 정렬해서 가장 큰 값들부터 탐색하는 것이다.




왜 `range(0,len(delta)-1,2)` ? 두칸씩 이동하나?

→ xor 은 반드시 두 개씩 짝지어야 하기 때문에, 2칸씩 이동한다.

- delta[0] + delta[1], delta[2] + delta[3], … 이런식으로 두 개씩 묶어서 판단하는 구조이다.

```python
[5, 3, 2, -1, -4]
 → (5 + 3), (2 + -1), (-4 + ?)
```



왜 `delta[i] + delta[i + 1] > 0` 체크?

→ 두 노드를 xor했을 때 총합이 증가해야만 실제로 xor을 적용할 가치가 있다.
'''
