class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i,j = 0,0
        size_first,size_second = len(firstList),len(secondList)
        res = []
        
        while i < size_first and j < size_second:
            if firstList[i][0] > secondList[j][1]:
                j += 1
                continue
            elif secondList[j][0] > firstList[i][1]:
                i += 1
                continue
            res.append([max(firstList[i][0],secondList[j][0]),min(firstList[i][1],secondList[j][1])])
            if firstList[i][1] == secondList[j][1]:
                i += 1
                j += 1
            elif firstList[i][1] > secondList[j][1]:
                j += 1
            else:
                i += 1
                
        return res
        