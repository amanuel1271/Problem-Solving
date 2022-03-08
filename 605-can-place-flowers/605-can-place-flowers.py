class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        can_place = 0
        size = len(flowerbed)
        
        if size == 1:
            return True if (n <= 1 and not flowerbed[0] or n == 0) else False
        
        if flowerbed[0] == 0 and flowerbed[1] == 0:
                can_place += 1
                flowerbed[0] = 1
        
        for i in range(1,size-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                can_place += 1
                flowerbed[i] = 1
        
        if flowerbed[size-2] == 0 and flowerbed[size-1] == 0:
            can_place += 1
            flowerbed[size-2] = 1

        return can_place >= n
            
        