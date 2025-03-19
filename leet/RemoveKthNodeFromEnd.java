/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
  public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0, head);
    ListNode left = dummy;

    ListNode right = head;
    // move right to a point where it is at a distance of k from left so that when right goes to null, left will be at the node we want to delete
    while(n-- > 0 && right != null){
      right = right.next;
    }

    while(right != null){
      left = left.next;
      right = right.next;
    }

    left.next = left.next.next;
    return dummy.next;
  }
}