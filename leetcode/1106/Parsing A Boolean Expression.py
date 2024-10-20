# solution 1
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        operand_stack = []
        operator_stack = []

        for exp in expression:
            if exp == "|" or exp == "&" or exp == "!":
                operator_stack.append(exp)
            elif exp == ")":
                now = operator_stack.pop()
                tmp = operand_stack[-1]
                if tmp == "t" or tmp == True:
                    tmp = True
                elif tmp == "f" or tmp == False:
                    tmp = False

                while operand_stack[-1] != "(":
                    cur = operand_stack.pop()
                    if cur == "t" or cur == True:
                        cur = True
                    elif cur == "f" or cur == False:
                        cur = False

                    if now == "|":
                        tmp |= cur
                    elif now == "&":
                        tmp &= cur
                    elif now == "!":
                        tmp = not cur

                operand_stack.pop()
                operand_stack.append(tmp)

            elif exp == "t" or exp == "f" or exp == "(":
                operand_stack.append(exp)

        if operand_stack[0]:
            return True
        else:
            return False


# solution 2 - clean code
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        operand_stack = []
        operator_stack = []

        for exp in expression:
            if exp in "|&!":
                operator_stack.append(exp)
            elif exp == ")":
                operator = operator_stack.pop()
                operands = []

                # Collect operands until we find '('
                while operand_stack[-1] != "(":
                    cur = operand_stack.pop()
                    operands.append(cur == "t" or cur is True)

                operand_stack.pop()  # Remove the '('

                # Apply the operator to the collected operands
                if operator == "|":
                    result = any(operands)
                elif operator == "&":
                    result = all(operands)
                elif operator == "!":
                    result = not operands[0]  # '!' has only one operand

                operand_stack.append(result)

            elif exp in "tf(":
                operand_stack.append(exp == "t" if exp in "tf" else exp)

        return operand_stack[0]
