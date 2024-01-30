class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        
        numbers = []
        operators = ['+','*','-','/']

        for t in tokens:
            # print(numbers)
            
            if t not in operators:
                numbers.append(int(t))
            elif t in operators:

                a, b = numbers.pop(), numbers.pop()

                
                if t == '+':
                    numbers.append(b+a)
                elif t == '-':
                    numbers.append(b-a)
                elif t == '*':
                    numbers.append(b*a)
                elif t == '/':
                    numbers.append(int(float(b)/a))
                               
        return numbers[0]
