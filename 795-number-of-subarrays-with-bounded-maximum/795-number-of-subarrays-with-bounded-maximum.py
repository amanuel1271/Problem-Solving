class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        L_ind, R_ind, ans = -1, -1, 0
        for i, num in enumerate(nums):
            if num >= left: L_ind = i
            if num > right:  R_ind = i
            ans += L_ind - R_ind
        return ans