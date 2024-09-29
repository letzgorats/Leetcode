class AllOne:

    def __init__(self):
        self.count_dict = defaultdict(int)
        # self.sorted_dict = []
        self.max_key = ""
        self.min_key = ""

    def inc(self, key: str) -> None:
        self.count_dict[key] += 1

        # max_key 업데이트 (self.max_key = key):
        # 증가 연산에서 key의 값이 기존의 최댓값과 같거나 더 크다면,
        # 단순히 key를 max_key로 지정하는 것으로 충분
        # 현재 증가된 키의 값이 가장 크므로 추가적인 탐색이 필요 없다.
        if not self.max_key or self.count_dict[key] > self.count_dict[self.max_key]:
            self.max_key = key
        # min 처리를 안해주면, 중간에 value가 같아지는 경우에, 잘못된 min_key가 설정될 수 있다.
        # a->b(이 타이밍에 b로 min_key가 바뀔 수 있다는 뜻)->b->b->b->...
        # 최솟값의 경우는 여러 키가 같은 값을 가질 수 있고,
        # inc()나 dec() 연산에 따라 최솟값이 바뀔 가능성이 많다.
        # 때문에, 모든 키를 다시 검사하여 최솟값을 가진 키를 찾도록 하는 것이 필요하다.
        if not self.min_key or self.count_dict[key] <= self.count_dict[self.min_key]:
            self.min_key = min(self.count_dict, key=self.count_dict.get)

    def dec(self, key: str) -> None:
        if key in self.count_dict:
            self.count_dict[key] -= 1
            if self.count_dict[key] == 0:
                del self.count_dict[key]

        if not self.count_dict:
            self.max_key = self.min_key = ""
        else:
            if key == self.max_key:
                self.max_key = max(self.count_dict, key=self.count_dict.get)
            elif key == self.min_key:
                self.min_key = min(self.count_dict, key=self.count_dict.get)

    def getMaxKey(self) -> str:
        return self.max_key

    def getMinKey(self) -> str:
        return self.min_key

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()