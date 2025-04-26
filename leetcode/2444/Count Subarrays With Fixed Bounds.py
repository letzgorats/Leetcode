# solution 1 - (sliding window) - (736ms) - (2024.03.31)
class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        
        res = 0

        jmin = jmax = jbad = -1

        for idx, num in enumerate(nums):
            if not minK <= num <= maxK:
                jbad = idx
            
            if num == minK :
                jmin = idx
            if num == maxK :
                jmax = idx
            
            res += max(0, min(jmin,jmax)-jbad)
            # print("jmin=",jmin)
            # print("jmax=",jmax)
            # print("jbad=",jbad)
            # print(res)
        
        return res


# solution 2 - (double deque,sliding window) - (331ms) - (2025.04.26)

from collections import deque
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        count = 0
        left = 0

        dq_min = deque()
        dq_max = deque()

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                dq_min.clear()
                dq_max.clear()
                left = i + 1
                continue

            if minK <= nums[i] <= maxK:
                while dq_min and nums[dq_min[-1]] >= nums[i]:
                    dq_min.pop()
                dq_min.append(i)  # index 를 추가해야 함(값이 아니라)
                while dq_max and nums[dq_max[-1]] <= nums[i]:
                    dq_max.pop()
                dq_max.append(i)

            # print(dq_min, dq_max)

            if nums[dq_min[0]] == minK and nums[dq_max[0]] == maxK:
                # start 변수의 의미?
                # 현재 i(끝 점-오른쪽 점)까지 갈 때, 유효한 부분 배열이 시작할 수 있는 가장 왼쪽 위치
                start = min(dq_min[0], dq_max[0])
                count += (start - left + 1)

                # print(count)

        return count


'''
1.

"값"이 아니라 "인덱스"를 넣어야 한다.

왜냐하면, 나중에 "윈도우를 관리"할 때는, 
"어떤 인덱스의 값이 오래됐는지", "어떤 인덱스를 뺴야 하는지"를 알아야 한다.

덱에는 "인덱스"를 넣고, 실제 값 비교는 "nums[인덱스]"로 해야 한다.

2.

범위를 벗어나는 숫자 처리
=> nums[i] 가 minK ~ maxK 범위를 벗어나면, 현재까지 만든 슬라이딩 윈도우는 무효이다.
이때, dq_min, dq_max 를 비워야 한다.
동시에, 윈도우 왼쪽 포인터(left)를 i+1 로 옮겨야 한다.

3.

minK와 maxK 가 둘 다 포함됐는지 확인

부분 배열 하나가 유효하려면, 현재 윈도우 안에 minK 를 가진 인덱스와 maxK 를 가진 인덱스가 존재해야 한다.
그걸 확인하기 위해 
    -> dq_min 의 앞쪽 값이 minK 인지
    -> dq_max 의 앞쪽 값이 maxK 인지 
둘 다 체크해야 한다.

이 로직이 있어야 "answer += 가능한 시작점 수"를 세어줄 수 있다.


4.

하나의 부분 배열이 유효하려면, 그 안에 minK 도 있어야 하고, maxK 도 있어야 한다.

그런데, minK 가 왼쪽에 있을 수도 있고, maxK가 더 왼쪽에 있을 수도 있다.
=> 둘 중에 "늦게 나온 것" 이후부터 유효해진다!

예를 들어,

인덱스    | 0 | 1        | 2        |    3     |    4     | 5
값(nums) | 3 | 2 (minK) | 5 (maxK) | 2 (minK) | 5 (maxK) | 7 (범위 밖)

지금 i=4(nums[4] = 5) 라고 해보면,
dq_min = [3] -> (index : 3, nums[3] = 2)
dq_max = [4] -> (index : 4, nums[4] = 5)

그러면, dq_min[0] = 3, dq_max[0] = 4 이므로,
i=4 까지 윈도우를 봤을 때, minK 와 maxK 가 둘 다 포함된 가장 이른 위치는 3 or 4 중에 더 작은 쪽이다.
즉, start = min(3,4) = 3 !

정리하면,
start를 min(dq_min[0],dq_max[0]) 로 잡아야,
"둘 다(minK와 maxK)가 포함된 가장 빠른 시작점"을 알 수 있기 때문이다!

그리고 이 start부터 현재 i까지가 유효현 부분 배열이 되는것이다.


left 는 범위 벗어났던 순간 이후부터 현재까지 유효한 구간의 가장 왼쪽
start 는 minK, maxK 둘 다 포함되기 시작한 순간(= minK,maxK 가 둘 다 포함되기 시작한 right 라고 받아들이면 됨.)
'''
            



        

 
            



        
