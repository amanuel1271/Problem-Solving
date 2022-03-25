class Node:
    def __init__(self,key,value):
        self.key,self.value = key,value
        self.prev = self.next = None

        



class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict() # key to Node
        self.capacity = capacity
        self.left,self.right = Node(-math.inf,-math.inf),Node(math.inf,math.inf)
        self.left.next,self.right.prev = self.right,self.left
        
        
        
    def remove(self,node):
        prev,next_ = node.prev,node.next
        prev.next,next_.prev = next_,prev
    
    def insert(self,node):
        prev = self.right.prev
        prev.next,node.prev = node,prev
        self.right.prev,node.next = node,self.right
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value  
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        new_node = Node(key,value)
        self.cache[key] = new_node
        self.insert(new_node)
        
        if len(self.cache) > self.capacity:
            remove_node = self.left.next
            self.remove(remove_node)
            del self.cache[remove_node.key]
            
        
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)