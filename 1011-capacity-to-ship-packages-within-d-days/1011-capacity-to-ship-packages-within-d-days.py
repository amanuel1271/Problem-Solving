class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def can_ship(capacity):
            count = 0
            days_taken = 1
            for weight in weights:
                if count + weight <= capacity:
                    count += weight
                else:
                    count  = weight
                    days_taken += 1
            
            return days_taken <= days
                
            
        left,right = max(weights),sum(weights)
        
        while left < right:
            mid = left + (right-left)//2
            
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
                
        return right
            
            