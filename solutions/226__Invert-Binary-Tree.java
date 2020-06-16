/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        
        TreeNode right = invertTree(root.right);
        TreeNode left  = invertTree(root.left);
        
        root.left = right;
        root.right = left;

        return root;
    }      
}

//Time Complexity: O(N) where N = # of nodes
//Space Complexity: O(h) where h = height of binary-tree where h = log(N). --> O(log(N))
