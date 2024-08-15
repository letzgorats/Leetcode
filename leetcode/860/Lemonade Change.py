class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        have = {5: 0, 10: 0, 20: 0}

        for bill in bills:

            have[bill] += 1
            change = (bill - 5)
            if change != 0:

                if change // 20 <= have[20]:
                    have[20] -= (change // 20)
                    change = (change % 20)
                if change // 10 <= have[10]:
                    have[10] -= (change // 10)
                    change = (change % 10)
                if change // 5 <= have[5]:
                    have[5] -= (change // 5)
                    change = (change % 5)

            if change != 0:
                return False

        return True