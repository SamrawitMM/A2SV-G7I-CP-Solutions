# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        count = 0
        current = head

        node_val = []
        while current:
            count += 1
            node_val.append(current.val)
            current = current.next

        n = count
        print(node_val)
        twin_pair_sum = 0
        max_twin_sum = float('-inf')
        for i in range(count):
            pair = n - i  - 1
            if pair < count:
                pair_sum = node_val[i] + node_val[pair]
                max_twin_sum = max(pair_sum, max_twin_sum)

        return max_twin_sum
