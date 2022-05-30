class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        stat = Counter(s1)
        length1 = len(s1)
        length2 = len(s2)

        index = 0
        while index <= length2 - length1:
            substat = Counter(s2[index:index+length1])
            if stat == substat:
                return True
            index += 1

        return False