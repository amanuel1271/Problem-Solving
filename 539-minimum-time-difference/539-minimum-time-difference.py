class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def get_time(time_str):
            hr,minute = time_str.split(":")
            return int(hr),int(minute)
        
        def time_diff(time1,time2):
            times = [time1,time2]
            times.sort()
            early,later = times[0],times[1]
            if later[0] - early[0] < 12 or (later[0]-early[0] == 12 and early[1] >= later[1]):
                return 60 * (later[0] - early[0]) + (later[1] - early[1])
            
            return (early[0] + (23 - later[0]) ) * 60 + (early[1] + 60 - later[1])
            
        
        times,min_time_diff = [],float('inf')
        for time in timePoints:
            times.append(get_time(time))
            
        times.sort()
        for i in range(len(times)): 
            min_time_diff  = min(min_time_diff,time_diff(times[i],times[i-1]))
        return min_time_diff
        
        