# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        prev = None
        curr = head

        while curr:
            # save the currents next node
            next_node = curr.next
            # reverse the pointer
            curr.next = prev
            # move our previous
            prev = curr
            curr = next_node

        return prev
