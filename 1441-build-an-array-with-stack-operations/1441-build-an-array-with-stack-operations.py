class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i,target_size,operation_lst = 0,len(target),[]
        
        for j in range(1,n+1):
            if i == target_size:
                break
            elif target[i] == j:
                operation_lst.append("Push")
                i += 1
            else:
                operation_lst.append("Push")
                operation_lst.append("Pop")
                
        return operation_lst
                
            
        