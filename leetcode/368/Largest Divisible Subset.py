# solution 1 - sort,dp - (266ms) - (2024.02.09)
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        nums = sorted(nums)
        n = len(nums)
        dp = [1] * n    
        parent = [-1] * n

        max_size = 0  # 최대 부분집합의 크기
        max_index = 0  # 최대 부분집합의 마지막 요소 인덱스

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_index = i

        # print(dp)
        # print(parent)
        # print(max_size)
        # print(max_index)
        # 최대 부분집합 재구성
        answer = []
        while max_index != -1:
            answer.append(nums[max_index])
            max_index = parent[max_index]


        return answer[::-1] 


# wrong answer
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()
        n = len(nums)
        dp = [1] * n  # num[i] 를 끝으로 하는 가장 큰 "완전한 divisible subset" 의 길이
        # print(dp)

        subsets = list()

        for i in range(n):
            s = [nums[i]]
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    s.append(nums[j])
                    dp[i] = max(dp[i], dp[j] + 1)
            # print(s)
            subsets.append(s)

        # print(dp)
        print(subsets)
        answer = max(subsets, key=len)
        return answer

'''
하나의 연결된 chaing 을 쌓는 것이 아니라, 그 때 그 때 나뉘어 떨어지는 수를 무작위로 추가하는 느낌
-> 결과적으로 실제 subset 조건을 완전히 보장하지 못함.
(ex) nums = [4,8,10,240] 일 때, 
nums[i] 가 240일 때, 추가된 [4,8,10,240] 이 답이 되어버리는데,
10 % 4 != 0 나 10 % 8 != 0 처럼 서로 완전한 divisible subset 이 아니게 된다.
nums[i] % nums[j] == 0 만으로 전체가 서로 배수 관계인지는 알 수 없기 때문에, 

prev[i] = 그 subset 에서 nums[i] 앞에 있었던 숫자의 인덱스를 저장하는 배열이 필요하다.

'''


# solution 2 - sort,dp,index,backtrack - (179ms) - (2025.04.06)
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()
        n = len(nums)
        dp = [1] * n  # num[i] 를 끝으로 하는 가장 큰 "완전한 divisible subset" 의 길이
        # print(dp)

        prev = [-1] * n  # nums[i] 바로 앞에 붙을 수 있는 수의 인덱스를 저장하는 배열

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

        # print(dp)
        # print(prev)
        # dp 에서 가장 긴 길이를 가진 부분을 먼저 찾고
        idx = dp.index(max(dp))
        # 해당 인덱스의 prev 를 파도타기 추적
        answer = []
        while prev[idx] != -1:
            answer.append(nums[idx])
            idx = prev[idx]

        answer.append(nums[idx])

        return answer


'''
prev = [-1] * n 으로 초기화를 하는데, 조건을 만족할 때마다 prev[i] = j 형태로 갱신해나가면 된다.
이 뜻은 현재 i 번째 인덱스의 숫자를 보고 있는데, nums[i] % nums[j] == 0 이 가능한 경우 index를 j 로 갱신하는 
작업이다.

즉, dp[i] 는 nums[i] 까지 가능한 최대 길이를 말하고, 
prev[i] 는 그 길이의 경로에서 nums[i] 앞에 있어야 할 인덱스를 말한다.


정말 모든 divisble set 을 구하려면, dp 배열에서 가장 큰 값을 가지는 인덱스에서 시작해서 해당 인덱스의 prev 배열에서 시작하여
파도타기 느낌으로 prev 에 있는 인덱스를 타고타고 들어가면 해당 숫자로 이루어진 리스트는 모두 다 완전한 divisible 구성이 된다.

(ex) nums = [4,8,10,240]
nums[i]를 끝으로 하는 완전히 연결된 chain 길이 dp = [1,2,1,3] (240 % 10 에서는 이미 dp[3] = dp[2] + 1 = 2 인데, 
이미 3보다 작으니까 무시) 

즉, 240이 4,8,10 으로 모두 나눠지지만, "한 chain으로 이어질 수 있는 최대 길이" 만 따지는 것이므로,
10은 이전 연결이 없었기 때문에, dp[2] = 1 이고, 240에 붙이면 최대 2밖에 안되니까, 4->8->240 이런 식으로 연결된 chain 이 되어야만
dp[3] 이 커짐.

prev = [-1,0,-1,1] 

그럼, dp가 가장 큰 값이 3 이고 해당 인덱스는 3 이니까 nums[3] = 240 에서 출발해서 chain을 찾는 과정이다.
idx = 3
while prev[idx] != -1
    answer.append(nums[idx])
    idx = prev[idx]

return answer
'''
