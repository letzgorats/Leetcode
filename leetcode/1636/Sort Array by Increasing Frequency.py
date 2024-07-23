# solution 1
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        counts = {}
        for n in nums:
            counts[n] = counts.get(n,0) + 1

        counts = sorted(counts.items(),key=lambda x : (x[1],-x[0]))

        # print(counts)
        # res = []
        # for k,v in counts:
        #     for i in range(v):
        #         res.append(k)

        return [k for k,v in counts for _ in range(v)]

# solution 2
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        res = sorted(nums, key=lambda x: (counts[x], -x))

        # print(res)

        return res
