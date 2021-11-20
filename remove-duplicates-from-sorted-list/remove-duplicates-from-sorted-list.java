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
    public ListNode deleteDuplicates(ListNode head) {
        
        //list is sorted, hence we simply check if the next element is equal to the previous element. If it is, then we skip over that element since in a sorted list, we cannot have repeating elements.
        
        ListNode curr = head;
        ListNode prev = head;
        
        while(curr != null && curr.next != null){
            if(curr.val == curr.next.val){
                curr.next = curr.next.next;
            }
            else{
                curr = curr.next;
            }
        }
        
        return head;
   
        
    }
}
