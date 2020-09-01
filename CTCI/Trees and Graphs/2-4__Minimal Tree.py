# Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimal_tree(self, arr):
        if len(arr) < 1: 
            return

        mid =  arr[len(arr) // 2 - 1]
        root = Node(val=mid)
        root.left = self.minimal_tree(arr[:len(arr) // 2 - 1])
        root.right = self.minimal_tree(arr[len(arr)// 2:])
        return root


arr = [2, 3, 7, 13, 20, 25, 31]
s = Solution()
print(s.minimal_tree(arr).right.right.right.val)
#