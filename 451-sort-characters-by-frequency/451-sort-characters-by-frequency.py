class Solution:
    def frequencySort(self, s: str) -> str:
        info = []
        freq_ = Counter(s)
        ALPHASIZE,DIGITSIZE = 26,10
        
        for alpha in 'abcdefghijklmnopqrstuvwxyz':
            info.append((-1 * freq_[alpha],alpha))
            info.append((-1 * freq_[alpha.upper()],alpha.upper()))
            
        for digit in '0123456789':
            info.append((-1 * freq_[digit],digit))
        
        heapify(info)
        ans = ''

        
        for i in range(ALPHASIZE * 2 + DIGITSIZE):
            count,ch = heappop(info)
            ans += (ch * (-1 * count))
            
        return ans