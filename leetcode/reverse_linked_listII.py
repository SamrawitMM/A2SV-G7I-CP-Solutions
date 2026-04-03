# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(next=head)
        prev_out = dummy

        for _ in range(left-1):
            prev_out = prev_out.next


        current = prev_out.next
        prev_in = None
        tail = current

        for _ in range(right - left+1):
            nxt = current.next
            current.next = prev_in
            prev_in = current
            current = nxt


        prev_out.next = prev_in
        tail.next = current


        return dummy.next



        



            

        
