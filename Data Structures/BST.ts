type BNode = {
    value: number;
    left: BNode | null;
    right: BNode | null;
}

function BinarySearchTree(curr: BNode, value: number): boolean {
    if (curr == null) {
        return false
    }

    if (curr.value == value) {
        return true
    }

    if (curr.value > value) {
        return BinarySearchTree(curr.left, value)
    } else {
        return BinarySearchTree(curr.right, value)
    }
}
