class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges : return [0]

        graph, seen = defaultdict(set), [False] * n

        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        leaves, new_leaves, in_degree = [], [], []

        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
            in_degree.append(len(graph[i]))
        
        while n > 2 :

            for leaf in leaves:
                for adj in graph[leaf]:
                    in_degree[adj] -= 1
                    if in_degree[adj] == 1:
                        new_leaves.append(adj)
            n -= len(leaves)
            leaves = new_leaves[:]
            new_leaves = []

        return leaves
