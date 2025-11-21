import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Set;



  public class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;
  TreeNode(int x) { val = x; }
  }

class Solution {
  private void findParent(TreeNode root, Map<TreeNode, TreeNode> map) {
    Queue<TreeNode> q = new LinkedList<>();
    q.add(root);
    while (!q.isEmpty()) {
      TreeNode node = q.remove();
      if (node.left != null) {
        map.put(node.left, node);
        q.add(node.left);
      }
      if (node.right != null) {
        map.put(node.right, node);
        q.add(node.right);
      }
    }
  }

  public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    Map<TreeNode, TreeNode> parentMap = new HashMap<>();
    findParent(root, parentMap);
    Set<TreeNode> ancestors = new HashSet<>();
    while (p != null) {
      ancestors.add(p);
      p = parentMap.get(p);
    }

    while (q != null) {
      if (ancestors.contains(q)) {
        return q;
      }
      q = parentMap.get(q);
    }
    return null;

  }
}