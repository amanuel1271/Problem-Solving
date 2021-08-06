#  Leetcode medium
#  subsets

def n_length_combo(lst, n):
        if n == 0:
            return [[]]

        l =[]
        for i in range(0, len(lst)):

            m = lst[i]
            remLst = lst[i + 1:]

            for p in n_length_combo(remLst, n-1):
                l.append([m]+p)

        return l



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = [[],nums]
        length = len(nums)
        
        for i in range(1,length):
            for elem in n_length_combo(nums,i):
                final.append(elem)
        
        return final
        


