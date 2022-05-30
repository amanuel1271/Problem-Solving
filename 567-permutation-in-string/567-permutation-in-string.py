class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        stat = Counter(s1)
        ans = [stat[chr(ord('a') + i)] for i in range(26)]
        
        
        length1 = len(s1)
        length2 = len(s2)

        index = 0
        while index <= length2 - length1:
            substat = Counter(s2[index:index+length1])
            subans = [substat[chr(ord('a') + i)] for i in range(26)]
            if subans == ans:
                return True
            index += 1

        return False