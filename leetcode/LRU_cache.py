class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # add right after the dummy head
    # order matters here
    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev = node.prev
        newNode = node.next
        prev.next = newNode
        newNode.prev = prev


    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)

    # when we want to remove the least used one
    def pop_tail(self):
        tail = self.tail.prev
        self.remove_node(tail)
        return tail
        
        
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # else: 
        node = self.cache[key]
        # recently accessed will be added to the front
        self.move_to_head(node)
        return node.val

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            # recently accessed will be added to the front
            self.move_to_head(node)
            
        else:
            if len(self.cache) >= self.capacity:
                # remove the least used one -> key
                tail = self.pop_tail()
                del self.cache[tail.key]
            # add the new node here
            node = Node(key, value)
            self.cache[key] = node
            # make it at the front
            self.add_node(node)
                



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



