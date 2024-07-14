# stack solution
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [{}]
        i = 0

        while i < len(formula):

            if formula[i] == "(":
                stack.append({})
                i += 1
            elif formula[i] == ")":
                top = stack.pop()
                i += 1
                i_start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                num = int(formula[i_start:i] or 1)
                for name,v in top.items():
                    stack[-1][name] = stack[-1].get(name,0) + num * v
            else:
                i_start = i
                i += 1
                while i < len(formula) and formula[i].islower():
                    i += 1
                name = formula[i_start:i]
                i_start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                num = int(formula[i_start:i] or 1)
                stack[-1][name] = stack[-1].get(name,0) + num


        return ''.join(name + (str(stack[0][name])if stack[0][name] > 1 else '') for name in sorted(stack[0]))


