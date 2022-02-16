class Solution:
    
    def tolist(self,head):
        vals = []
        start = head
        while start != None:
            vals.append(start.val)
            start = start.next
        return vals
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = self.tolist(head)
            
        def mergeSort(lst):
            size = len(lst)
            if size <= 1:
                return lst
            
            l = mergeSort(lst[:size//2])
            r = mergeSort(lst[size//2:])
            i,j,k = 0,0,0
            lenl,lenr = len(l),len(r)
            res = [0] * (lenl + lenr)
            
            
            while i < lenl and j < lenr:
                if l[i] < r[j]:
                    res[k] = l[i]
                    i += 1
                    k += 1
                else:
                    res[k] = r[j]
                    j += 1
                    k += 1
            
            while i < lenl:
                res[k] = l[i]
                i += 1
                k += 1
            
            while j < lenr:
                res[k] = r[j]
                j += 1
                k += 1
                
            return res
        
        
        def puttoLinkedList(lst):
            prev = None
            for i in range(len(lst)-1,-1,-1):
                prev = ListNode(lst[i],prev)
            return prev
                
        
        return puttoLinkedList(mergeSort(vals))
