class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        prefix_sum_dict = {-1:0}
        size,sum_ = len(cardPoints),0
        minn = math.inf
        
        
        for i in range(size):
            sum_ += cardPoints[i]
            prefix_sum_dict[i] = sum_
            if i < size-k-1:
                continue
                
            minn = min(minn,sum_ - prefix_sum_dict[i-(size-k)])
        
        return sum(cardPoints) - minn
        

            
        