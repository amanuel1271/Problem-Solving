class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        
        @lru_cache(None)
        def calculate_people(knows_date):
            if knows_date > n:
                return 0
            
            count = 1 if knows_date + forget > n else 0 # himself knows
            for date in range(knows_date + delay,knows_date + forget):
                count += calculate_people(date)
                
            return count
                
        ans = calculate_people(1)
        return ans % (10**9 + 7)
        