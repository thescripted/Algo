class Solution:
    def shortest_bridge(self, A):
        MAX_ROW, MAX_COLUMN = len(A), len(A[0])

        def neighbors(row, column):
            for n_row, n_col in ((row + 1, column), (row, column + 1), (row - 1, column), (row, column - 1)):
                if 0 <= n_row < MAX_ROW and 0 <= n_col < MAX_COLUMN:
                    yield n_row, n_col

        def get_components():
            visited = set()
            two_islands = []
            for r, row in enumerate(A):
                for c, value in enumerate(row):
                    if value and (r, c) not in visited:
                        #depth-first-search
                        dfs_stack = [(r, c)]
                        island = {(r,c)}
                        while dfs_stack:
                            node = dfs_stack.pop()
                            for row, column in neighbors(*node):
                                if A[row][column] and (row, column) not in island:
                                    dfs_stack.append((row, column))
                                    island.add((row, column))
                        two_islands.append(island)
                        visited = visited | island 
            return two_islands
        source, target = get_components()

        distance = 0
        batch = []
        queue = [(item, 0) for item in source]
        done = set(source)
        while queue:
            batch = queue
            queue = []
            node, d = queue.pop(0)
            if node in target:
                return d - 1
            for row, column in neighbors(*node):
                if (row, column) not in done:
                    queue.append(((row, column), d + 1))
                    done.add((row, column))


s = Solution()

M = [[0,1,0],[0,0,0],[0,0,1]]
print(s.shortest_bridge(M))