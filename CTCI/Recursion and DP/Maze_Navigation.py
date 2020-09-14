class Solution:
    def __init__(self):
        pass

    def navigate_maze(self, matrix):
        row = 0
        col = 0
        source = matrix[row][col] 
        visited = set()
        return reversed(self._dfs(row, col, matrix, visited))

    def _dfs(self, row, col, matrix, visited):

        if (row, col) in visited:
            return False
        
        visited.add((row, col))

        if not self._isValid(row, col, matrix):
            return False
        
        if matrix[row][col] == 100:
            path = []
            path.append((row, col))
            return path

        path_down = self._dfs(row + 1, col, matrix) # False or Node
        if path_down is not False:
            path_down.append((row, col))
            return path_down

        path_left = self._dfs(row, col + 1, matrix) # False or Node
        if path_left is not False:
            path_left.append((row, col))
            return path_left

        return False

        
    def _isValid(self, row, col, matrix):
        """Determine if node is a valid node to traverse"""
        if matrix[row][col] == None:
            return False
        
        if row >= len(matrix) or col >= len(matrix[0]):
            return False
        
        return True
