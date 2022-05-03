class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def common_prefix(s1,s2):
            i,j,len1,len2 = 0,0,len(s1),len(s2)
            while i < len1 and j < len2 and s1[i] == s2[j]:
                i += 1
                j += 1
                
            return '' if i == 0 else s1[:i]
            
        common = strs[0]
        for word in strs[1:]:
            common = common_prefix(common,word)
            if not common:
                break
                
        return common
        
        
        