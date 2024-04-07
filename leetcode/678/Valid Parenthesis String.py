# solution1 - greedy

class Solution(object):
    def checkValidString(self, s):
        '''
    low: '*'를 ')' 또는 빈 문자열로 간주했을 때 가능한 열린 괄호 '('의 최소 개수입니다.
    high: '*'를 '('로 간주했을 때 가능한 열린 괄호 '('의 최대 개수입니다.
    문자열을 순회하면서 각 문자에 따라 low와 high를 업데이트합니다:

    만약 문자가 '('라면, low와 high 모두를 증가시킵니다.
    만약 문자가 ')'라면, low와 high 모두를 감소시킵니다. 단, low가 0보다 클 경우에만 감소시켜 음수가 되지 않도록 합니다.
    만약 문자가 '*'라면, low를 감소(0보다 클 때만)시키고 high를 증가시킵니다.
    순회 중에 high가 0보다 작아진다면, 괄호를 올바르게 닫을 수 없으므로 false를 반환합니다.
    순회가 끝난 후 low가 0이라면, 괄호를 올바르게 닫을 수 있는 방법이 존재하는 것이므로 true를 반환합니다. 그렇지 않다면 false를 반환합니다.

    중요한 사항
    순회 중에 low가 음수가 되면, 0으로 재설정합니다.
    음수인 low는 닫힌 괄호가 열린 괄호보다 많다는 것을 의미하며,
    '*'를 빈 문자열로 간주할 수 있기 때문에 과도한 닫힌 괄호를 무시할 수 있습니다.
    이 방법은 '*'의 모호성을 효과적으로 처리하면서 열린 괄호의 가능한 개수 범위(low에서 high)
    를 추적합니다. 범위에 0이 포함되면 문자열을 올바른 괄호 문자열로 간주할 수 있습니다.
    이 탐욕적 방법은 문자열을 한 번만 순회하기 때문에 시간 복잡도는 O(n), 
    공간 복잡도는 O(1)입니다. 여기서 n은 문자열의 길이입니다.
'''
        
        stack = []
        low , high = 0,0

        for i,st in enumerate(s):

            if st == "(":
                low += 1
                high += 1
            elif st == ")":
                if low > 0 :
                    low -= 1
                high -= 1
            elif st == "*":
                if low > 0 :
                    low -= 1
                high += 1

            if high < 0:
                return False
        
        return low == 0
'''
'(' 문자 처리
문자가 '('일 때, low와 high를 모두 증가시키는 이유는, 열린 괄호가 추가됨으로써 필요한 닫힌 괄호의 수가 하나 더 필요하게 되기 때문입니다. 
이는 괄호의 최소 개수(low)와 최대 개수(high)가 모두 증가한다는 것을 의미합니다.

')' 문자 처리
문자가 ')'일 때, low와 high를 모두 감소시키는데, 이는 닫힌 괄호가 하나 추가되어 열린 괄호와 매칭되어야 함을 의미합니다. 
low를 감소시킬 때는 low가 0보다 클 경우에만 감소시키는데, 이는 열린 괄호 없이 닫힌 괄호만으로 괄호의 균형을 맞출 수 없기 때문입니다. 
low가 음수가 되는 것을 방지하며, high가 음수가 될 경우는 올바른 괄호 문자열을 형성할 수 없다는 의미이므로 false를 반환합니다.

'*' 문자 처리
'*' 문자는 '(' , ')' 또는 빈 문자열 중 하나를 나타낼 수 있습니다. 
따라서, low를 감소시키고(닫힌 괄호로 간주하거나 빈 문자열로 간주), high를 증가시키는(열린 괄호로 간주) 방식으로 처리합니다. 
여기서 low가 0보다 클 때만 감소시키는 이유는 열린 괄호가 없는 상태에서 닫힌 괄호를 추가하는 것은 올바른 괄호 문자열을 형성할 수 없기 때문입니다.
high가 언제든지 음수가 되면, 닫힌 괄호가 너무 많아 올바른 괄호 문자열을 형성할 수 없음을 의미하므로 false를 반환합니다.

결론
순회가 끝난 후 low가 0이면, 모든 열린 괄호에 대응하는 닫힌 괄호를 찾을 수 있는 하나 이상의 방법이 존재한다는 의미이므로 true를 반환합니다.
low가 0이 아니라면, 남아 있는 열린 괄호를 닫을 수 없으므로 false를 반환합니다.
이 알고리즘은 '*' 문자로 인한 여러 가능성을 고려하면서도, 올바른 괄호 문자열을 효과적으로 판단할 수 있는 방법을 제공합니다.
'''

# solution2 - stack
class Solution(object):
    def checkValidString(self, s):

        open_stack = []
        star_stack = []
    
        for i, st in enumerate(s):
            if st == '(':
                open_stack.append(i)
            elif st == '*':
                star_stack.append(i)
            else:  # char == ')'
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
    
        # 남은 '('와 '*' 매칭 처리
        while open_stack and star_stack:
            if open_stack[-1] < star_stack[-1]:
                open_stack.pop()
                star_stack.pop()
            else:
                return False
    
        return not open_stack
