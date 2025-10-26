# solution 1 - (design,implementation) - (56ms) - (2025.10.27)
from collections import defaultdict
from typing import List

class Bank:

    def __init__(self, balance: List[int]):

        self.accounts = defaultdict(int)
        for idx, b in enumerate(balance):
            self.accounts[idx + 1] = b

    def transfer(self, account1: int, account2: int, money: int) -> bool:

        if account1 < len(self.accounts) + 1 and account2 < len(self.accounts) + 1:
            if money <= self.accounts[account1]:
                self.accounts[account1] -= money
                self.accounts[account2] += money
                return True
            else:
                return False

        return False

    def deposit(self, account: int, money: int) -> bool:

        if account > len(self.accounts) + 1:
            return False

        self.accounts[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:

        if account < len(self.accounts) + 1 and money <= self.accounts[account]:
            self.accounts[account] -= money
            return True

        return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)