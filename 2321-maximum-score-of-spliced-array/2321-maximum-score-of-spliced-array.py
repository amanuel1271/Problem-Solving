class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        val = max(sum(nums1),sum(nums2))
        diff1 = [nums1[i]-nums2[i] for i in range(len(nums1))]
        diff2 = [-x for x in diff1]
        
        def kadane(arr):
            global_max = -math.inf
            localmax = 0

            for num in arr:
                localmax = max(0,localmax + num) 
                global_max = max(global_max,localmax)
            return global_max
                
        
        return max(val,sum(nums2) + kadane(diff1),sum(nums1) + kadane(diff2))
            
        