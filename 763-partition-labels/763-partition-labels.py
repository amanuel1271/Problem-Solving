class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        def char_to_index():
            letter_to_indices = dict()
            for i in range(len(s)):
                if s[i] in letter_to_indices:
                    letter_to_indices[s[i]].add(i)
                else:
                    letter_to_indices[s[i]] = {i}
            return letter_to_indices
        
        ch_index = char_to_index()
        
        ans,visited = [],set()
        start,end = 0,-math.inf
        
        for i in range(len(s)):
            if s[i] not in visited:
                end = max(end,max(ch_index[s[i]]))
                visited.add(s[i])
                
            if i == end:
                ans.append(end-start + 1)
                start,end = i+1,-math.inf
                continue
                
        if start < len(s):
            ans.append(end-start+1)
            
        return ans
                
            