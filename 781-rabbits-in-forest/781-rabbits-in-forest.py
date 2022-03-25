class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        samecolor = defaultdict(int)
        for answer in answers:
            samecolor[answer] += 1
            
        count  = 0
        for ans,cnt in samecolor.items():
            count += math.ceil(cnt/(ans + 1)) * (ans + 1)
            
        return count
            
        
        
        