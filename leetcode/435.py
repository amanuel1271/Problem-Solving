class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_inte = sorted(intervals,key = lambda tup: (tup[0],tup[1]))
        
        count = 0
        non_overlap = [sorted_inte[0]]
        
        
        for x,y in sorted_inte[1:]:
            if non_overlap[-1][0] <= x < non_overlap[-1][1]:
                if non_overlap[-1][0] <= y < non_overlap[-1][1]:
                    non_overlap[-1] = [x,y]
                count += 1

            else:
                non_overlap.append([x,y])
                
        return count
