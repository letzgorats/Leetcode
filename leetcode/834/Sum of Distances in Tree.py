class Solution(object):
    def sumOfDistancesInTree(self, n, edges):

        answer = [0] * n
        graph = [[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # 첫 번째 DFS: 각 노드의 서브트리 크기와 서브트리 내 노드들로부터의 거리 합을 계산
        count = [1] * n
        dist_sum = [0] * n
        
        def first_dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    first_dfs(child, node)
                    count[node] += count[child]
                    dist_sum[node] += (dist_sum[child] + count[child])
        
        first_dfs(0, -1)  # 루트 노드에서 시작, 부모는 없음

        # print(count)
        # print(dist_sum)

        # # 두 번째 DFS: 각 노드를 루트로 하는 거리의 합 계산
        answer = [0] * n
        answer[0] = dist_sum[0]  # 루트 노드의 거리 합
        
        def second_dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    # child의 거리 합은 node의 거리 합에서 child 서브트리를 빼고 나머지 트리를 더해 재계산
                    answer[child] = answer[node] - count[child] + (n - count[child])
                    second_dfs(child, node)
        
        second_dfs(0, -1)  # 루트 노드에서 시작

        return answer




        
