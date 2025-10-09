# solution 1 - (dp,prefix sum) - (13755ms) - (2025.10.09)
from typing import List
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:

        n, m = len(skill), len(mana)
        time = [0] * n

        for x in mana:
            time[0] = time[0] + skill[0] * x
            for i in range(1, n):
                time[i] = max(time[i], time[i - 1]) + skill[i] * x
            for i in range(n - 2, -1, -1):
                time[i] = time[i + 1] - skill[i + 1] * x

        return time[-1]

'''
1) 정방향 스윕 : "대기허용"으로 일단 흘려보내기

- 현재 물약의 마나를 x라고 할 때,
- time[0] += p_{0,j} : 마법사 0은 본인 가용 시각 이후 p_{0,j} 만큼 처리 -> 완료 시각
- i>=1 : 마법사 i는
    - 본인 가용 시각 time[1] 과
    - 이전 마법사(i-1)가 이번 물약을 끝낸 시각 time[i-1]
    - 둘 중 더 늦은 시각부터 시작해서 p_{i,j}만큼 처리 -> 완료 시각
- 이 단계가 끝나면, time[i] 는 "대기 가능 모델에서의 이번 물약 완료 시각" 이 된다.

2) 역방향 스윕 : "즉시 전달(no-wait)"로 압축

- time[i+1]는 마법사 i+1 의 완료시각
- 그로부터 p_{i+1,j} (i+1의 처리시간)을 빼면, i+1의 시작 시간이 된다.
- 그 시작 시각을 i의 완료 시각으로 덮어쓴다 => i가 끝나는 즉시 i+1 이 시작하도록 강제(즉시 전달)
- 이걸 위로 쭉 전파하면, 모든 인접하는 마법사 쌍에서 대기가 사라진 "no-wait"스케줄이 된다.

이렇게 압축을 해도 앞선 물약들의 완료 제약은 깨지지 않는다.
왜냐하면 정방향에서 이미 max(time[i],time[i+1])로 "더 늦은 쪽"에 맞춰 잡았고,
역방향에서는 "붙이기"만 해서 오른쪽(i+1)의 시작 시각보다 더 이르게 만들지 않기 때문이다.
결과적으로 "이번 물약"은 가능한 한 최소 간격으로 동기화된 상태가 되고, 그 상태의 time이 다음 물약 시작 시의 가용시각이 된다.

'''