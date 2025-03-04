# solution 1 - math - (0ms) - (2025.03.04)
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        while n != 0:

            if n % 3 == 2:
                return False
            n //= 3

        return True

'''
The question is essentially asking us to figure out whether a number can be 
represented by a base 3 ternary system where none of the powers of 3 are
duplicated, i.e, the powers of 3 must be "distinct".

Note that for example 3, n = 21 can be represented as 2*(3^2) + 1*)3^1) + 0 *(3^0),
or (210)_3 in base 3.
The 2 coefficient here is the problem because that means we don't have distinct powers of 3.
Try doing the same thing you would when converting a number to binary, 
except, instead of using 2, we are using 3 as the base here.
'''