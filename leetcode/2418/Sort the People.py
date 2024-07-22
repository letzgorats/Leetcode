class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = sorted(zip(heights, names), key=lambda x: -x[0])
        return [x[1] for x in res]