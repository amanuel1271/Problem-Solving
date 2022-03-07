class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        e = sorted(heights)
        count = 0
        
        for i in range(len(heights)):
            if heights[i] != e[i]:
                count += 1
        return count
        