# TLE - (2025.07.29)
from typing import List
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:

        n = len(nums)
        suffix_or = [0] * n
        suffix_or[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_or[i] = suffix_or[i + 1] | nums[i]

        # print(suffix_or)

        # suffix_or[i] = i 이후에서 만들 수 있는 최대 OR 값
        # curr_or : i 부터 시작해서 or을 누적해 나가며 목표값이 나올 때까지 j 를 확장
        # j 를 확장하다가 처음으로 목표 or 값이 완성되면, 그 길이를 저장

        answer = [0] * n
        for i in range(n):
            curr_or = 0
            for j in range(i, n):
                curr_or |= nums[j]
                if curr_or == suffix_or[i]:
                    answer[i] = j - i + 1
                    break  # 더 짧은 길이는 없으니 바로 멈춤

        # print(answer)

        return answer

# solution 1 - (bit manipulation) - (1471ms) - (2025.07.29)
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:

        n = len(nums)
        last = [0] * 32  # 각 비트 위치에서, 가장 최근에 1 이 나온 인덱스를 저장할 배열
        answer = [0] * n

        for i in range(n - 1, -1, -1):
            for b in range(32):
                if (nums[i] >> b) & 1:
                    last[b] = i  # b번째 비트가 i 에 있음

            farthest = i
            for b in range(32):
                # 필요한 비트가 있는 가장 먼 index 까지 봐야 함
                farthest = max(farthest, last[b])

            answer[i] = farthest - i + 1  # 최소 길이 계산

        return answer


'''
last = [0] * 32
--> 각 비트 위치(0~31)에서, 가장 최근에 1이 나온 인덱스를 저장할 배열
nums[j]가 ...0010 이면, 1번 비트가 1 이나 last[1] = j

1. 바깥 루프 : i 를 거꾸로 보며 서브배열 시작점으로 설정
for i in range(n-1,-1,-1):
-> i 를 뒤에서부터 앞까지 이동
-> 이유? 뒤에서 누적하면서 비트 위치를 최신으로 갱신하기 위해서!

2. 현재 숫자의 비트를 확인
for b in range(32):
    if (nums[i] >> b) & 1:
        last[b] = i
-> nums[i] 의 b 번째 비트가 켜져 있으면, 그 비트의 마지막 등장 위치를 현재 i로 업데이트
-> 즉, 현재 숫자가 가진 비트들을 기록

3. i 부터 시작해서 'or 최댓값'을 만들기 위한 가장 먼 j 찾기
farthest = i
for b in range(32):
    farthest = max(farthest,last[b])
-> 지금까지 기록된 last[b] 값들 중에서 가장 멀리 있는 비트 위치를 찾음
-> 이유? or 최댓값을 만들기 위해 그 비트는 반드시 필요하므로, 최소한 그 지점까지는 서브배열에 포함되어야 하기 때문!

4. 최소길이 계산
-> i부터 farthest 까지 보면서 최대 or 을 만들 수 있으니, 길이는 "farthest-i+1"

지금 nums[i]에서 출발해서, 나중에 OR 최대값을 만들기 위해 필요한 비트들이 어디 있는지를 추적하고,
그 비트들이 등장하는 가장 멀리 있는 인덱스까지 봐야 하므로
-> 그만큼의 최소 길이를 answer[i]로 저장하는 것!
'''

