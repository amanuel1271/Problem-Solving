class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurence_visited = set()
        
        occurence = Counter(arr)
        
        for _,cnt in occurence.items():
            if cnt in occurence_visited:
                return False
            occurence_visited.add(cnt)
            
        return True