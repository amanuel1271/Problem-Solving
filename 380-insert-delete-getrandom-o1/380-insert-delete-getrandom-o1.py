class Node:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class RandomizedSet:

    def __init__(self):
        self.left_end = Node(0)
        self.right_end =  Node(0)
        self.left_end.right = self.right_end
        self.right_end.left = self.left_end
        self.hashmap = {} # maps values to Nodes

        
        

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        
        new_node = Node(val)
        right = self.left_end.right
        new_node.right,right.left = right,new_node
        new_node.left,self.left_end.right = self.left_end,new_node
        self.hashmap[val] = new_node
        return True
        
        

    def remove(self, val: int) -> bool:
        if not val in self.hashmap:
            return False
        

        node = self.hashmap[val]
        left,right = node.left,node.right
        left.right,right.left = right,left
        del self.hashmap[val]
        return True
        
        

    def getRandom(self) -> int:
        
        return choice(list(self.hashmap.keys()))
        
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()