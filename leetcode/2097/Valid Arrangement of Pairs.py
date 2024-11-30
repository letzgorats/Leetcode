class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:

        graph = defaultdict(list)
        inOutDeg = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            inOutDeg[start] += 1  # out-degree
            inOutDeg[end] -= 1  # in-degree

        # print(inOutDeg)

        # Finding starting node
        startNode = pairs[0][0]
        for node in inOutDeg:
            if inOutDeg[node] == 1:  # if 1 start node. no 1? any node
                startNode = node
                break

        path = []

        def dfs(curr):
            while graph[curr]:
                next_node = graph[curr].pop()
                dfs(next_node)
                path.append((curr, next_node))

        dfs(startNode)
        # print(path)
        return path[::-1]
