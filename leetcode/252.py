class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        
        intervals.sort(key = lambda x : x[0])
        
        minStart,maxEnd = intervals[0]
        for start,end in intervals[1:]:
            if (start >= minStart and end <= maxEnd) or (start < minStart and end > maxEnd) or (minStart <= start < maxEnd and end > maxEnd) or (minStart < end <= maxEnd and start < minStart):
                return False
            
            minStart,maxEnd = min(start,minStart),max(end,maxEnd)
        
        return True
