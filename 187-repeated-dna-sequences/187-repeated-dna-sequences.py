class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = collections.defaultdict(int) 
        for i in range(len(s)-9):
            sequences[s[i:i+10]] += 1
            
        return [key for key, value in sequences.items() if value > 1] 
        