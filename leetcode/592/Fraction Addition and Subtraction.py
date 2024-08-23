from fractions import Fraction
import re
from math import lcm

class Solution:
    def fractionAddition(self, expression: str) -> str:

        ln = list(map(int,re.findall(r"\/(\w+)+",expression)))
        # print(ln)
        lm = lcm(*ln)
        # print(lm)
        m = Fraction(str(eval(expression))).limit_denominator(lm)
        # print(m)

        return f"{m.numerator}/{m.denominator}"