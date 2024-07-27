from collections import defaultdict


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(original)
        graph = defaultdict(list)
        for i in range(n):
            graph[original[i]].append((changed[i], cost[i]))

        print(graph)


