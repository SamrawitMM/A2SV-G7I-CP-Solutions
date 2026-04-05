"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
            
        dic = {}
        current = head
        while current:
            newNode = Node(current.val)
            dic[current] = newNode
            current = current.next
        
        current = head
        while current:
            copy = dic[current]
            copy.next = dic.get(current.next)
            copy.random = dic.get(current.random)
            current = current.next

        return dic[head]

        
        
