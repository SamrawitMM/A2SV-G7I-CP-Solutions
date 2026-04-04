# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        lessNode, greaterNode = ListNode(), ListNode()
        left_tail, right_tail = lessNode, greaterNode

        while head:
            if head.val < x:
                left_tail.next = head
                left_tail = left_tail.next
            
            else:
                right_tail.next = head
                right_tail = right_tail.next

            head = head.next

        
        left_tail.next = greaterNode.next
        right_tail.next = None

        return lessNode.next

        
