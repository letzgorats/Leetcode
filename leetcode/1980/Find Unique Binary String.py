# first solution - backtracking(2023.11.16)
class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
       
        def addstr(temp):
            if len(temp) == n:
                if temp not in nums:
                    return temp
            else:
                result = addstr(temp + "0")
                if result:
                    return result
                return addstr(temp + "1")

        n = len(nums[0])
        nums = set(nums)
        # print(nums)

        temp = ""
        candi = set()
        candi.add(addstr(temp))
        for c in candi:
            return c        


# 여기서 함수는 먼저 temp + "0"을 사용하여 재귀 호출을 합니다. 만약 이 호출이 유효한 결과(즉, None이 아닌 값)를 반환하면, 해당 결과를 다시 반환합니다.
# 만약 temp + "0"을 사용한 재귀 호출이 유효한 결과를 반환하지 않으면(즉, None을 반환하면), temp + "1"을 사용하여 다른 재귀 호출을 시도합니다.
# 이렇게 수정하면, addstr 함수는 항상 유효한 이진 문자열을 찾거나, 모든 가능성을 탐색한 후에 None을 반환하게 됩니다. 그 결과 candi 리스트는 None 대신 유효한 이진 문자열들로 채워질 것입니다.

'''
Understanding None Return in Recursive Functions

1. Default Return Value: In Python, a function returns None by default if it doesn't encounter a return statement.

2. Recursive Call: addstr(temp + "0") or addstr(temp + "1") represent recursive calls. These calls return a value only when the string temp reaches the desired length n.

3. Condition Not Met: If the length of temp does not reach n, or it does but the created string is already present in the nums set, the function terminates without hitting a return statement, thus returning None.

4. Processing the Result of Recursive Calls: If the result of addstr(temp + "0") is None, meaning this path did not lead to a valid string, then addstr(temp + "1") is called next. This attempts a different path.

5. Exploring All Possibilities: This process continues until all possible binary string combinations are explored. If a suitable string is found, it is returned; otherwise, None is ultimately returned.

<Example>
Consider an example where n=2 and nums={"00", "01"}:

1. Initially, addstr("") is called.
2. Then, addstr("0") is called.
3. Next, addstr("00") is called and returns None as it exists in nums.
4. addstr("01") is also called and returns None for the same reason.
5. After exploring all paths for addstr("0"), addstr("1") is called.
6. Among addstr("10") and addstr("11"), whichever finds a valid string returns it, else None is returned.
'''

# TLE - (2025.02.20)
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        bits = len(nums[0])
        def backtracking(idx, cur):
            nonlocal answer

            if len(cur) == bits and cur not in nums:
                answer.append(cur)
                return

            for j in range(idx + 1, bits + 1):
                backtracking(j, cur + "0")
                backtracking(j, cur + "1")

        answer = []
        backtracking(0, "")

        return answer[0]

'''
2023.11.16 에 이은 2025.02.20 두 번째 풀이

역시 backtracking 활용
TLE 가 난 코드는 모든 answer 리스트를 찾느라 TLE 걸리는 것.
그러면, answer 리스트에 들어갈만한 수가 나오면 바로 리턴하려면 어떻게 해야 할까. 
'return cur' 을 하면 None 값이 나왔다. 
왜? -> 탈출조건에서의 return 은 해당 백트래킹에 대한 반환 값이기 때문에, return cur 을 하면
해당 백트래킹 호출문 다음으로 간다. 그러므로 거기서도 return 값을 해줘야 한다.
다시 고친 정답코드(두 번째 풀이)는 아래와 같다.
'''
# second soultion - backtracking(2025.02.20)
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        bits = len(nums[0])

        def backtracking(idx, cur):

            if len(cur) == bits and cur not in nums:
                return cur

            for j in range(idx + 1, bits + 1):

                res = backtracking(j, cur + "0")
                if res:
                    return res
                res = backtracking(j, cur + "1")
                if res:
                    return res

            # return None  # 끝까지 찾지 못한 경우는 None 처리하는데, 해당 코드는 굳이 안써줘도 된다.

        return backtracking(0, "")

# 더 효율적인 풀이 - 칸토어 대각선 방법
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        '''
        칸토어의 대각선 방법 O(N)
        칸토어의 대각선 방법을 적용하면, `nums의 i번째 요소의 i번째 비트를 뒤집어서`
        새로운 숫자를 만들면 항상 nums에 없는 숫자가 된다는 점을 활용할 수 있다.

        각 문자열을 행렬로 보면
        (ex) nums = ["111","011","001"]

        1 1 1
        0 1 1
        0 0 1

        여기서 대각선 방향의 비트를 뒤집은 새로운 숫자를 만들면 반드시 nums 에 없는 문자열이 된다.
        즉, '111' 을 뒤집은 '000' 은 nums 에 존재하지 않는다.
        이 방법은 nums 를 순회하지 않고도 찾을 수 있는 강력한 방법이다.
        = nums[i][i] 값을 변경하는 순간 기존 리스트의 모든 요소와 최소 하나의 비트에서 다름이 보장되기 때문.
        ->  특정 방식으로 숫자를 생성하면 원래 리스트에 절대 포함될 수 없음을 증명하는 방법 : 칸토어 대각선 방법

        이 방법은 특히 "고유한 아이디 생성 문제나 조합이 부족할 때"에도 활용될 수 있는 강력한 테크닉이다.

        * 칸토어 대각선 방법
        칸토어의 대각선 방법은 게오르크 칸토어(Georg Cantor)가 "무한 집합의 크기(기수, cardinality)"
        를 비교할 때 사용한 증명 기법이다. 이를 이용해 특정 집합이 다른 집합보다 크거나 다름을 보일 수 있다.
        이 방법은 특히 실수 집합이 자연수 집합보다 더 크다는 것을 증명하는 데 사용되었으며,
        컴퓨터 과학에서도 유일한 값을 찾는 문제에서 활용할 수 있다.
        '''
        res = ""
        for i in range(len(nums)):
            if nums[i][i] == "0":
                res += "1"
            else:
                res += "0"

        return res

