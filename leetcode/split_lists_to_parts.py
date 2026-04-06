# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        
        size = count // k
        extra = count % k
        res = []
        current = head
        for i in range(k):
            split_h = current
            added_size = size + 1 if extra >= 1 else size

            if current:
                # the last node next connects to none 
                # therefore we will be using a length of - 1
                for _ in range(added_size-1):
                    current = current.next

                nextNode = current.next
                current.next = None
                current = nextNode

                if extra > 0:
                    extra -= 1

            res.append(split_h)


        return res

        
