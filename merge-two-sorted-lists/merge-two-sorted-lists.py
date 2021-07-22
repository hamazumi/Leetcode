# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # traverse list 1
        
        #traverse list 2
        
        # at each sttep, compare values at each node
        
        # put the lower value in the new list
        
        #traverse through that list
        new_node = ListNode()
        
        temp = new_node
        
        while l1 is not None and l2 is not None:
            
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            
            temp = temp.next
        
        if l1 is not None:
            temp.next = l1
        else:
            temp.next = l2
            
        return new_node.next