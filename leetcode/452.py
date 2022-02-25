class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda p: p[0])
        overlap = [points[0]]
        ans = 1
        
        for point in points[1:]:
            if overlap[-1][0] <= point[0] <= overlap[-1][1]:
                overlap[-1] = [point[0],min(overlap[-1][1],point[1])]
            else:
                overlap.append(point)
                ans += 1
        
        return ans
