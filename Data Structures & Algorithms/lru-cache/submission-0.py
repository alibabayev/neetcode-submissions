class Node:

    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value

        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # key -> Node
        self.cache = {} 

        # sentinel nodes to prevent complex edge-case implementations
        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node: Node) -> None:
        previous = node.prev
        following = node.next

        previous.next = following
        following.prev = previous
    
    def _insert_to_end(self, node: Node) -> None:
        last_node = self.right.prev
        last_node.next = node
        self.right.prev = node

        node.next = self.right
        node.prev = last_node
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._insert_to_end(node)
        return node.val

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]

            node.val = value
            self._remove(node)
            self._insert_to_end(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self._insert_to_end(node)

        if len(self.cache) > self.capacity:
            node = self.left.next
            del self.cache[node.key]
            self._remove(node)

             

        
