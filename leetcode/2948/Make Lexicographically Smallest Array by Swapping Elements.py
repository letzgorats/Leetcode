# solution - sorting,index
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        n = len(nums)
        # 값 기준으로 정렬
        nums2 = sorted([(nums[i], i) for i in range(n)])

        # 스왑 가능한 그룹을 저장할 리스트
        # 각 그룹은 연결된 인덱스들의 집합을 나타낸다.
        indices = []
        # 결과 리스트
        answer = [0] * n

        for i in range(n):
            # 다른 그룹이라면 [] 추가
            if i == 0 or nums2[i][0] - nums2[i - 1][0] > limit:
                indices.append([])
            # 인덱스 추가
            indices[-1].append(nums2[i][1])

        for index in indices:
            sortedIndex = sorted(index)
            for j in range(len(index)):
                answer[sortedIndex[j]] = nums[index[j]]

        return answer

# solution 2 - DSU