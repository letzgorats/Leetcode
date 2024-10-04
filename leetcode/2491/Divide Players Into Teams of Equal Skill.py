class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()
        n = len(skill)
        pre = (skill[0] + skill[n - 1])
        total = 0

        for i in range(n // 2):

            if pre != (skill[i] + skill[n - i - 1]):
                return -1
            else:
                total += (skill[i] * skill[n - i - 1])

        return total