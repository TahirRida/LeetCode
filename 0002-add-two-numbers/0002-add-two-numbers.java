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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int div = 0;
        int reste = 0;
        ListNode curr = new ListNode();
        ListNode res = curr;
        while(l1 != null && l2!= null){
            int somme = l1.val + l2.val+ div;
            div = somme/10;
            reste = somme%10;
            res.next = new ListNode(reste);
            res = res.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        while(l1 != null){
            int somme = l1.val + div;
            div = somme/10;
            res.next = new ListNode(somme%10);
            res = res.next;
            l1 = l1.next;
        }
        while(l2 != null){
            int somme = l2.val + div;
            div = somme/10;
            res.next = new ListNode(somme%10);
            res = res.next;
            l2= l2.next;
        }
        if(div != 0){
            res.next = new ListNode(div);
            res = res.next;
        }
        return curr.next;
    }
}
