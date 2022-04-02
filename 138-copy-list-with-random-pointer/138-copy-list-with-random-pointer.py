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
        if head is None:
            return None
        
        
        map_nodes = {None: None}
        new_head = Node(head.val)
        old_ptr,new_ptr = head,new_head
        map_nodes[old_ptr] = new_ptr

        while old_ptr:
            if old_ptr.next in map_nodes:
                next_node = map_nodes[old_ptr.next]
            else:
                next_node = Node(old_ptr.next.val) if old_ptr.next else None
                map_nodes[old_ptr.next] = next_node
                
            new_ptr.next = next_node
            
            if old_ptr.random in map_nodes:
                random_node = map_nodes[old_ptr.random]
            else:
                random_node = Node(old_ptr.random.val) if old_ptr.random else None
                map_nodes[old_ptr.random] = random_node
            
            new_ptr.random = random_node
            
            old_ptr = old_ptr.next
            new_ptr = next_node
            
        return new_head
            
            
        