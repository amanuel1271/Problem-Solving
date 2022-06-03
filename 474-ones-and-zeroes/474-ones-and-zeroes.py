class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
          
        @lru_cache(None)
        def count(i,m_left,n_left):
            if i >= len(strs) or m_left < 0 or n_left < 0:
                return 0
            
            size = len(strs[i])
            zeroes = strs[i].count('0')
            ones = size - zeroes
            
            if m_left - zeroes < 0 or n_left - ones < 0:
                return count(i+1,m_left,n_left)
            
            return max(count(i+1,m_left,n_left),1 + count(i+1,m_left-zeroes,n_left-ones))
            
            
        return count(0,m,n)