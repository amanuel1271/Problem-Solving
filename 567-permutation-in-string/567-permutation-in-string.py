class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def compare_arrays(arr1,arr2):
            for i in range(26):
                if arr1[i] != arr2[i]:
                    return False 
            return True
        
        s2 = 'z' + s2
        size1,size2 = len(s1),len(s2)
        if size1 > size2:
            return False
        
        freq_count,window_array = [0 for _ in range(26)],[0 for _ in range(26)]
        for ch in s1:
            freq_count[ord(ch)- ord('a')] += 1
        for ch in s2[:size1]:
            window_array[ord(ch)- ord('a')] += 1
            
        i = 0
        while i <= size2-size1-1:
            window_array[ord(s2[i]) - ord('a')] -= 1
            i += 1
            window_array[ord(s2[i + size1-1]) - ord('a')] += 1
            
            if compare_arrays(window_array,freq_count):
                return True
            
        
        return False