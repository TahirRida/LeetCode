# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l3 = ListNode()
        curr = l3
        div,reste = 0,0
        while l1 != None and l2 != None:
            somme = l1.val+l2.val+div
            div = somme//10
            reste = somme%10
            curr.next = ListNode(reste)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1 != None:
            somme = l1.val+div
            div = somme//10
            reste = somme%10
            curr.next = ListNode(reste)
            curr = curr.next
            l1 = l1.next
        while l2 != None:
            somme = l2.val+div
            div = somme//10
            reste = somme%10
            curr.next = ListNode(reste)
            curr = curr.next
            l2 = l2.next
        if(div != 0):
            curr.next = ListNode(div)
        return l3.next
            
            
        
        