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
    boolean result = false;
    void solve(TreeNode root, TreeNode sub){
        if(root == null || sub == null){
            return;
        }
        if(root.val == sub.val){
            if(answer(root, sub)){
                result = true;
                return;
            }
        }
        solve(root.left, sub);
        solve(root.right, sub);
    }
    boolean answer(TreeNode root, TreeNode sub){
        if(root == null && sub == null){
            return true;
        }
        else if (root == null){
            return false;
        }
        else if (sub == null){
            return false;
        }
        if(root.val != sub.val){
            return false;
        }
        return answer(root.right, sub.right) && answer(root.left, sub.left);
    }
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        solve(root, subRoot);
        return result;
    }
}