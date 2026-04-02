# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pevious=None
        current=head
        while current:
            next_curr = current.next
            current.next=pevious
            pevious = current
            current = next_curr
        return pevious


        

        

                


                
            




        