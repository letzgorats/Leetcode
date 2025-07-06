# solution1 - (hash table,counter) - (305ms) - (2025.07.06)
from collections import Counter
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums1_cnt = Counter(nums1)
        self.nums2_cnt = Counter(nums2)

    def add(self, index: int, val: int) -> None:

        x = self.nums2[index]
        self.nums2[index] += val
        self.nums2_cnt[x] -= 1
        self.nums2_cnt[x + val] += 1

    def count(self, tot: int) -> int:

        answer = 0
        for num1 in self.nums1:
            if tot - num1 in self.nums2_cnt:
                answer += self.nums2_cnt[tot - num1]

        return answer

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)