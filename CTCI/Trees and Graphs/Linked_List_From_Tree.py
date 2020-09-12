# Create a linked list for each level of a binary tree

def solution(root):
    result = []
    parents = []
    current = [root]
    while current:
        result.append(current)
        parents = list(current)
        current = []
        for parent in parents:
            if parent.left is not None:
               current.append(parent.left)
            if parent.right is not None:
                current.append(parent.right)
    return result