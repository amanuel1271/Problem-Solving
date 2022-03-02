class Solution:
    def frequencySort(self, s: str) -> str:
        info = []
        ALPHASIZE,DIGITSIZE = 26,10
        
        for alpha in 'abcdefghijklmnopqrstuvwxyz':
            info.append((-1 * s.count(alpha),alpha))
            info.append((-1 * s.count(alpha.upper()),alpha.upper()))
            
        for digit in '0123456789':
            info.append((-1 * s.count(digit),digit))
        
        heapify(info)
        ans = ''

        
        for i in range(ALPHASIZE * 2 + DIGITSIZE):
            count,ch = heappop(info)
            ans += (ch * (-1 * count))
            
        return ans
