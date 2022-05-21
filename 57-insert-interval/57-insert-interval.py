class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        def binary_search():
            l,r = 0,len(intervals)-1
            ans = -1
            
            while l <= r:
                mid = (l+r)//2
                if intervals[mid][0] == newInterval[0]:
                    return mid
                elif intervals[mid][0] < newInterval[0]:
                    ans = mid
                    l = mid + 1   
                else:
                    r = mid - 1
                    
            return ans
        
        def not_intersect(range1,range2):
            return (range1[0] > range2[1] or range2[0] > range1[1])
        
        greatest_index = binary_search()
        if greatest_index  == -1:
            intervals.insert(0,newInterval)
            greatest_index = 0
        if not_intersect(newInterval,intervals[greatest_index]):
            intervals.insert(greatest_index + 1,newInterval)
            greatest_index += 1
        
        index = greatest_index + 1
        intervals[greatest_index] = [min(intervals[greatest_index][0],newInterval[0]),max(intervals[greatest_index][1],newInterval[1])]
        while index < len(intervals):
            if not_intersect( intervals[greatest_index], intervals[index]):
                break  
            intervals[greatest_index] = [min(intervals[greatest_index][0],intervals[index][0]),max(intervals[greatest_index][1],intervals[index][1])]
            intervals.pop(index)
            
        return intervals
        
        
        
        
        
                    
        