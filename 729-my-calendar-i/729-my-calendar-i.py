class MyCalendar:

    def __init__(self):
        self.sorted_by_start = []
        
    def lower_binary_search(self,key):
        index = -1
        l,r = 0,len(self.sorted_by_start)-1
        
        while l <= r:
            mid = (l+r)//2
            
            if self.sorted_by_start[mid][0] <= key:
                index = mid
                l = mid+1
            else:
                r = mid-1    
        return index
    
    def upper_binary_search(self,key):
        index = -1
        l,r = 0,len(self.sorted_by_start)-1
        
        while l <= r:
            mid = (l+r)//2
            
            if self.sorted_by_start[mid][0] >= key:
                index = mid
                r = mid-1
            else:
                l = mid+1
        return index
    
    def no_overlaps(self,tup1,tup2):
        x1,x2 = tup1
        x3,x4 = tup2
        return x3 >= x2 or x4 <= x1
        

    def book(self, start: int, end: int) -> bool:
        lower_index = self.lower_binary_search(start)
        if lower_index != -1:
            boundary_1 = self.sorted_by_start[lower_index]
            boundary_2 = (start,end)
        
            if  not self.no_overlaps(boundary_1,boundary_2):
                return False

            
        upper_index = self.upper_binary_search(start)
        if upper_index != -1:
            boundary_1 = self.sorted_by_start[upper_index]
            boundary_2 = (start,end)
            if not self.no_overlaps(boundary_1,boundary_2):
                return False
            
        elif upper_index == -1 and lower_index == -1:
            self.sorted_by_start.append((start,end))
            return True
        
        index = max(lower_index+1,upper_index)
        self.sorted_by_start.insert(index,(start,end))
        return True
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)