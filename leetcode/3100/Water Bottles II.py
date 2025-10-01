# solution 1 - (greedy,math) - (29ms) - (2025.10.02)
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:

        drink = numBottles
        full = 0
        empty = numBottles

        while True:
            # print(full,empty,numExchange,drink)
            if empty < numExchange: # 바꿀 수 없으면
                if full <= 0:
                    break
                drink += full  # 마시고
                empty += full  # 빈 병 생기고
                full = 0  # 풀 병 0
            else:
                empty -= numExchange  # 바꿀 수 있으면 풀병으로 교환
                full += 1  # 풀 병 +1
                numExchange += 1  # 교환 기준값 + 1

        return drink
