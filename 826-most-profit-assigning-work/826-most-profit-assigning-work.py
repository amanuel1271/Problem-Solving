class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = zip(difficulty,profit)
        sorted_jobs = sorted(jobs)
        

        sorted_worker = sorted(worker)
        size = len(sorted_jobs)
        
        i = best_profit = total_best_profit = 0
        
        for skill in sorted_worker:
            while i < size and skill >= sorted_jobs[i][0]:
                best_profit = max(best_profit,sorted_jobs[i][1])
                i += 1
            
            total_best_profit += best_profit
        
        return total_best_profit
    
        
        
            
        