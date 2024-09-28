class MyCircularDeque:

    def __init__(self, k: int):
        self.circular_deque = deque(maxlen=k)
        self.max_length = k

    def insertFront(self, value: int) -> bool:
        if len(self.circular_deque) != self.max_length:
            self.circular_deque.appendleft(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.circular_deque) != self.max_length:
            self.circular_deque.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.circular_deque) != 0:
            self.circular_deque.popleft()
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.circular_deque) != 0:
            self.circular_deque.pop()
            return True
        return False

    def getFront(self) -> int:
        if len(self.circular_deque) != 0:
            return self.circular_deque[0]
        return -1

    def getRear(self) -> int:
        if len(self.circular_deque) != 0:
            return self.circular_deque[-1]
        return -1

    def isEmpty(self) -> bool:
        if len(self.circular_deque) == 0:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.circular_deque) == self.max_length:
            return True
        return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()