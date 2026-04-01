# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast = head
        slow = head
        cycle = False

        # Phase 1
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                cycle = True
                break

        if cycle:
            # Phase 2
            ptr = head
            while ptr:
                ptr = ptr.next
                slow = slow.next

                if ptr == slow:
                    return slow

        if not cycle:
            return None

        

        
