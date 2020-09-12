class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


class Solution:
    def solve(self, input_items, total_weight):
        # build out a 2D matrix.
        matrix = []
        for item in input_items:
            matrix.append([0 for _ in range(total_weight + 1)])
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                value = self._best_choice(matrix, input_items[row], row, col)
                matrix[row][col] = value
        
        return matrix[len(matrix) - 1][len(matrix[0]) -1]

    def _best_choice(self, matrix, item, row, col):
        _item_up = matrix[row-1][col-item.weight] if (row - 1 >= 0 and col-item.weight >= 0) else 0
        _item_curr = item.value if item.weight <= col else 0
        select_item = _item_up + _item_curr
        pick_above = matrix[row-1][col] if (row - 1 >= 0 ) else 0
        return max(select_item, pick_above)

s = Solution()

item_arr = [Item(5, 60), Item(3, 50), Item(4, 70), Item(2, 30)]
max_value = s.solve(item_arr, 5)
print(max_value)