class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """

        graph = defaultdict(list)
        indegree = [0] * n

        for node in range(n):
            left, right = leftChild[node], rightChild[node]

            if left != -1:
                graph[node].append(left)
                indegree[left] += 1
            if right != -1:
                graph[node].append(right)
                indegree[right] += 1
            
        root_candidate = [node for node in range(n) if indegree[node] == 0]

        # root is only one!
        if len(root_candidate) != 1:
            return False
        
        root = root_candidate[0]

        queue = [root]
        seen = set([root])

        while queue:

            node = queue.pop(0)

            for child in graph[node]:
                if child in seen:
                    return False
                seen.add(child)
                queue.append(child)
                # print(seen)

        return len(seen) == n 
