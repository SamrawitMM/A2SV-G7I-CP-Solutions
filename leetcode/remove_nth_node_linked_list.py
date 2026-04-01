# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         # Approach 1

#         if not head:
#             return head
        
#         count = 0
#         current = head
#         while current:
#             current = current.next
#             count += 1

#         remove = count - n
#         i = 0

#         dummy = ListNode(next=head)
#         current = dummy

#         while current.next and i < remove:
#             current = current.next
#             i += 1

#         current.next = current.next.next

#         return dummy.next

        # Approach 2

        dummy = ListNode(next= head)

        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next


        






            
        
