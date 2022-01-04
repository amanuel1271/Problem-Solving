class Solution {
public:
    void unlink(ListNode *next_node,ListNode *find_next){
        ListNode *unlink = next_node;
        while (unlink && unlink->next != find_next)
            unlink = unlink->next;
        if (unlink)
            unlink->next = NULL;    
    }
    
    void reorderList(ListNode *head) {
        if (head == NULL)
            return;
        
        ListNode *find_next = head;
        ListNode *next_node = head->next;
        
        if (next_node == NULL)  return;
        while (find_next->next)  find_next = find_next->next;
        
        if (next_node != find_next){
            head->next = find_next;
            find_next->next = next_node;
        }
        unlink(next_node,find_next);
        reorderList(next_node);  
    }
};
