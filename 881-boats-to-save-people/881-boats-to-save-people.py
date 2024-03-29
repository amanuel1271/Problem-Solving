class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        left,right = 0,len(people)-1
        boatsreq  = 0
        
        while right > 0 and people[right] == limit:
            right -= 1
            boatsreq += 1
            
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            
            boatsreq += 1
        
        return boatsreq
        