# solution 1 - hash,sort - (79ms) - (2025.03.27)
from collections import Counter, defaultdict
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        pre = defaultdict(int)
        suff = Counter(nums)
        n = len(nums)
        dominant_x = max(suff, key=suff.get)

        for i, num in enumerate(nums):
            if nums[i] == dominant_x:
                pre[dominant_x] += 1
                suff[dominant_x] -= 1
                # 길이 == i + 1
                if (i + 1) < 2 * pre[dominant_x] and n - (i + 1) < 2 * (suff[dominant_x]):
                    return i

        return -1

# solution 2 - hash, sort - (124ms) - (2025.03.27)
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        pre = defaultdict(int)
        suff = Counter(nums)
        n = len(nums)
        dominant_x = max(suff, key=suff.get)

        for i, num in enumerate(nums):

            # 일관되게 num 빈도수 처리
            pre[num] += 1
            suff[num] -= 1
            # 길이 == i + 1
            if (i + 1) < 2 * pre[num] and n - (i + 1) < 2 * (suff[num]):
                return i

        return -1

'''
max(iterable, key=기준함수) 패턴은 굉장히 자주 씀.
- iterable에 있는 각 요소 `x`에 대해 `func(x)` 값을 계산해서,
- 그 결과가 가장 큰 `x`를 반환하는 것.

dominant_x = max(suff, key=suff.get) 에서는 suff.get(x) 를 해서 그 값이 가장 큰 key 값(=x)을 반환하는 것
'''

# solution 3 - 여기서처럼 dominant_x 가 아니라 일관된 num 빈도수를 계산하려면 그냥 num 으로 하면 된다. - hash, sort - (103ms) - (2025.03.27)
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        pre = defaultdict(int)
        suff = Counter(nums)
        n = len(nums)
        # dominant_x = max(suff, key=suff.get)

        for i, num in enumerate(nums):

            # 일관되게 num 빈도수 처리
            pre[num] += 1
            suff[num] -= 1
            # 길이 == i + 1
            if (i + 1) < 2 * pre[num] and n - (i + 1) < 2 * (suff[num]):
                return i

        return -1