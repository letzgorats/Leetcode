class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]  # 곱을 저장하는 리스트(1로 초기화)

    def add(self, num: int) -> None:

        if num == 0:
            self.prefix = [1]  # 0 이 나오면 곱이 초기화되므로 새롭게 시작
        else:
            self.prefix.append(self.prefix[-1] * num)



    def getProduct(self, k: int) -> int:

        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]  # (마지막 값) / (k번째 앞 값)

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)