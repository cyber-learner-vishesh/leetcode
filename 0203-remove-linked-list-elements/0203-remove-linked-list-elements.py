# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    
        if head is None:
            return head
        
        
        temp_prev =head
        temp = head.next
        
        while temp:
            if temp.val == val:
                temp_prev.next = temp.next
                temp = temp.next
            else:
                temp_prev = temp
                temp = temp.next
        
        if head and head.val ==val:
            head= head.next
        return head



        

