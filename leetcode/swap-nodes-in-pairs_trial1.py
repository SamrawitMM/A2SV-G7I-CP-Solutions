# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        # Recursion
        def swapNodes(head):
            
            if head is None or head.next is None:
                return head
            
            
            first = head
            second = head.next
            
            
            first.next = self.swapPairs(second.next)
            second.next = first
            
            return second
        
        return swapNodes(head)
        
#         if head is None or head.next is None:
#             return head
            
#         dummy = ListNode(next=head)
#         prev = dummy
        
#         def swapNodes(prev):
            
            
#             if prev.next is None or prev.next.next is None:
#                 return dummy.next
            
#             first = prev.next
#             second = prev.next.next     
            
#             prev.next = second
#             first.next = second.next
#             second.next = first
            
            
            
#             return swapNodes(first)
        
        
        
#         return swapNodes(prev)
            
            
            
            

#         if head is None:
#             return head

#         dummy = ListNode(next=head)

#         prev = dummy

#         while prev.next and prev.next.next:

#             first = prev.next
#             second = first.next

#             prev.next = second
#             first.next = second.next
#             second.next = first

#             # the swapped second node is first
#             # we start iterating from that point
#             prev = first

            
            
        
#         return dummy.next



        