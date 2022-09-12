class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i,target_size,operation_lst = 0,len(target),[]
        j = 1
        
        while j <= n:
            if i == target_size:
                break
            elif target[i] == j:
                operation_lst.append("Push")
                i += 1
                j += 1
            else:
                for _ in range(target[i]-j):
                    operation_lst.append("Push")
                    operation_lst.append("Pop")
                j = target[i]
                
        return operation_lst
                
            
        