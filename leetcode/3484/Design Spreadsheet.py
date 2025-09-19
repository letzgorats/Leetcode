# solution 1 - (greedy,hash table,grid) - (154ms) - (2025.09.19)
class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadsheet = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:

        c, r = cell[0], int(cell[1:])

        self.spreadsheet[r - 1][ord(c) - 65] = value

    def resetCell(self, cell: str) -> None:
        self.spreadsheet[int(cell[1:]) - 1][ord(cell[0]) - 65] = 0

    def getValue(self, formula: str) -> int:

        self.formula = formula[1:]
        nums = list(self.formula.split('+'))

        if nums[0].isdigit() and nums[1].isdigit():  # 숫자+숫자
            return int(nums[0]) + int(nums[1])
        elif not nums[0].isdigit() and nums[1].isdigit():  # 수식+숫자
            c, r = nums[0][0], int(nums[0][1:])
            return self.spreadsheet[r - 1][ord(c) - 65] + int(nums[1])

        elif not nums[0].isdigit() and not nums[1].isdigit():  # 수식+수식
            c1, r1 = nums[0][0], int(nums[0][1:])
            c2, r2 = nums[1][0], int(nums[1][1:])
            return self.spreadsheet[r1 - 1][ord(c1) - 65] + self.spreadsheet[r2 - 1][ord(c2) - 65]

        else:  # 숫자+ 수식
            c, r = nums[1][0], int(nums[1][1:])
            return int(nums[0]) + self.spreadsheet[r - 1][ord(c) - 65]
# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)