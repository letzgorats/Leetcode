from collections import defaultdict
import heapq


class NumberContainers:

    def __init__(self):
        self.index_to_number = {}
        self.number_to_indices = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.index_to_number[index] = number
        heapq.heappush(self.number_to_indices[number], index)

        # print(self.number_to_indices)
        # print(self.index_to_number)

    def find(self, number: int) -> int:

        while self.number_to_indices[number]:  # 힙이 비어있지 않다면
            min_index = self.number_to_indices[number][0]
            if self.index_to_number.get(min_index) == number:
                return min_index
            heapq.heappop(self.number_to_indices[number])  # 유효하지 않은 index 제거

        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)