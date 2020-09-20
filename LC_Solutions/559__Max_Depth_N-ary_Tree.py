class Solution: #DFS Iterative
    def maxDepth(self, root: 'Node') -> int:
        stack = []
        if root:
            stack.append((root, 1))
        depth = 0
        while stack:
            node, d = stack.pop()
            depth = max(depth, d)
            for child in node.children:
                stack.append((child, d + 1))
        return depth

class Solution: # BFS Iterative
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        queue = [root]
        batch = []
        count = 0
        while queue:
            count = count + 1
            batch = queue
            queue = []
            for elem in batch:
                for child in elem.children:
                    if child is not None:
                        queue.append(child)
                
        return count

class Solution: # DFS Recursive
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        return self._dfs(root, 1)

    def _dfs(self, node, count):
        max_count = count
        for child in node.children:
            max_count = max(max_count, self._dfs(child, count + 1))
        
        return max_count
        