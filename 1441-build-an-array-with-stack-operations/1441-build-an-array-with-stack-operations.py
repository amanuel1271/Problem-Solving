class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i,target_size,operation_lst = 0,len(target),[]
        j = 1
        
        while i < target_size:
            if target[i] == j:
                operation_lst.append("Push")
                i += 1
                j += 1
            else:
                for _ in range(target[i]-j):
                    operation_lst.append("Push")
                    operation_lst.append("Pop")
                j = target[i]
                
        return operation_lst
                
            
        