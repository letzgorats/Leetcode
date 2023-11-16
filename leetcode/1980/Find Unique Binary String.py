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
