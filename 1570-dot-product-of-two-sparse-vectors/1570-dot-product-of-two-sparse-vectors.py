class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.notzero = set([i for i in range(len(nums)) if nums[i] != 0])
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        for i in range(len(vec.nums)):
            if i in self.notzero and vec.nums[i] == 0:
                self.notzero.remove(i)
                
        count = 0  
        while self.notzero:
            i = self.notzero.pop()
            count += self.nums[i] * vec.nums[i]
            
        return count
        
                
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)