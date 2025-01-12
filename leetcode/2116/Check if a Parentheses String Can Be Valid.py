class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        # 유효한 괄호 문자열은 반드시 짝수 길이여야 한다.
        if len(s) % 2 != 0:
            return False

        # left -> right : 열린 괄호와 자유로운 '_'로 유효성 확인
        open_cnt = 0  # 현재 열린 괄호와 '_' 의 총 개수
        for i in range(len(s)):
            if locked[i] == "0" or s[i] == "(":
                open_cnt += 1
            else:
                open_cnt -= 1

            # 닫힌 괄호가 열린 괄호를 초과하면 유효하지 않음
            if open_cnt < 0:
                return False

        print(open_cnt)

        # right -> left : 닫힌 괄호와 자유로운 '_'로 유효성 확인
        close_cnt = 0  # 현재 닫힌 괄호와 '_' 의 총 개수
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == "0" or s[i] == ")":
                close_cnt += 1
            else:
                close_cnt -= 1

            # 열린 괄호가 닫힌 괄호를 초과하면 유효하지 않음
            if close_cnt < 0:
                return False

        print(close_cnt)

        return True


'''
Q ) [왼쪽 -> 오른쪽] 검사가 True 라면, 만들 수 있는 문자열이 되는 것이 아닌가?
A ) 아니다. [왼쪽 -> 오른쪽] 검사만으로는 '_'가 열린 괄호로 처리된 결과가 유효하지 않을 수 있기 때문에 양방향 검사가 필요하다.
    [오른쪽 -> 왼쪽] 검사를 통해 '_'가 닫힌 괄호로 간주되어야 하는 상황도 확인해줘야 한다. 
'''