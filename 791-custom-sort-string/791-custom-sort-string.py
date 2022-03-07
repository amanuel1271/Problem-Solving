class Solution:
    def customSortString(self, order: str, s: str) -> str:
            order_dict  = {}
            for i in range(len(order)):
                order_dict[order[i]] = i
            
            slist = list(s)
            size = len(slist)
            
            for i in range(size-1,-1,-1):
                for j in range(i):
                    if slist[j] in order_dict and slist[j+1] in order_dict:
                        if order_dict[slist[j]] > order_dict[slist[j+1]]:
                            slist[j],slist[j+1] = slist[j+1],slist[j]
                    else:
                        slist[j],slist[j+1] = slist[j+1],slist[j]
            
            return ''.join(slist)
                
        
            
            
                
        