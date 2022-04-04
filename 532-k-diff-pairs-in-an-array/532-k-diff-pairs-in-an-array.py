class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        visited = set()
        unique = set()
        count = 0
        
        for num in nums:
            if num  - k in visited and (min(num - k,num),max(num-k,num)) not in unique:
                count += 1
                unique.add(((min(num - k,num),max(num-k,num))))
            
            if num + k in visited and (min(num + k,num),max(num + k,num)) not in unique:
                count += 1
                unique.add((min(num + k,num),max(num + k,num)))
                
            visited.add(num)
            
        
        return count
                
                
        