class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0, 1]
        if n == 1: return res
        
        idx = 1
        total = 1 << n
        
        while len(res) < total:
            if idx % 2 == 1:
                res.append(2 * res[idx] + 1)
                res.append(2 * res[idx])
            else:
                res.append(2 * res[idx])
                res.append(2 * res[idx] + 1)
            idx += 1
        return res
                    