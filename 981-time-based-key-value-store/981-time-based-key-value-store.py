
class KeyToStoreMax:
    def __init__(self,time,mapping = {}):
        self.timestamps = [time]
        self.mapping = mapping
        
def binary_search(times,target):
    left,right = 0,len(times)-1
    res = -1
    
    while left <= right:
        mid = (left + right) // 2
        if times[mid] == target:
            return mid
        elif times[mid] > target:
            right = mid - 1
        elif times[mid] < target:
            res,left = mid,mid+1
    return res



class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].timestamps.append(timestamp)
            self.map[key].mapping[timestamp] = value
            
        else:
            self.map[key] = KeyToStoreMax(timestamp)
            self.map[key].mapping[timestamp] = value
            
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ''
        
        res = binary_search(self.map[key].timestamps,timestamp)
        time = self.map[key].timestamps[res]
        return self.map[key].mapping[time] if res != -1 else ''
        
            
        
        
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)