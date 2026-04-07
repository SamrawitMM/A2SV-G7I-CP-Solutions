# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head

        dummy = ListNode(next=head)

        prev = dummy

        while prev.next and prev.next.next:

            first = prev.next
            second = first.next

            prev.next = second
            first.next = second.next
            second.next = first

            # the swapped second node is first
            # we start iterating from that point
            prev = first

            
            
        
        return dummy.next



        
