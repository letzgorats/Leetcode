# solution 1 - 12ms - O(2*n)
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        indegree = [0] * n
        for a,b in edges:
            indegree[b] += 1

        if indegree.count(0) == 1:
            return indegree.index(0)
        return -1

# solution 2 - 7ms - O(n)
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        indegree = [0] * n

        # 간선 정보를 기반으로 indegree 계산
        for u, v in edges:
            indegree[v] += 1

        # indegree가 0인 노드 찾기
        champions = [i for i in range(n) if indegree[i] == 0]

        # 챔피언이 유일한지 확인
        return champions[0] if len(champions) == 1 else -1