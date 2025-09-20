# TLE
class Router:

    def __init__(self, memoryLimit: int):
        self.router = deque(maxlen=memoryLimit)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:

        if [source, destination, timestamp] in self.router:  # duplicate packet
            return False
        else:
            self.router.append([source, destination, timestamp])
            return True

    def forwardPacket(self) -> List[int]:
        if self.router:
            return self.router.popleft()
        else:
            return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:

        cnt = 0
        for s, d, t in self.router:
            if startTime <= t <= endTime and d == destination:
                cnt += 1

        return cnt

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)


# solution 1 - (binary search,set,queue,deque) - (245ms) - (2025.09.20)
from collections import defaultdict, deque
import bisect
from typing import List
class Router:

    def __init__(self, memoryLimit: int):
        self.size = memoryLimit
        self.queue = deque()
        self.used_pac = set()
        self.l = 0
        self.destination_map = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        temp_p = (source, destination, timestamp)

        if temp_p in self.used_pac:  # duplicate
            return False
        if self.l >= self.size:
            old = self.queue.popleft()
            self.used_pac.remove(old)
            self.destination_map[old[1]].pop(0)
            self.l -= 1
        self.queue.append(temp_p)
        self.used_pac.add(temp_p)
        self.destination_map[destination].append(timestamp)
        self.l += 1
        return True

    def forwardPacket(self) -> List[int]:
        if self.l == 0:
            return []
        self.l -= 1
        p = self.queue.popleft()
        self.used_pac.remove(p)
        self.destination_map[p[1]].pop(0)
        return list(p)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:

        a = self.destination_map[destination]
        return bisect.bisect_right(a, endTime) - bisect.bisect_left(a, startTime)

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)