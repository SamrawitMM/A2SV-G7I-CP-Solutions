# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       
        # count the length of the list
        count = 0
        current = head
        while current:
            count += 1
            current = current.next

        

        if count < 2 or head is None:
            return head
        
        k %= count
        if k == 0:
            return head

        disconnect = count - k

        # second disconnected list
        tail2 = head
        for _ in range(disconnect-1):
            tail2 = tail2.next


        # start of the first disconnected list
        current = tail2.next
        tail2.next = None

        tail1 = current

        while tail1.next:
            tail1 = tail1.next

        tail1.next = head

        return current
