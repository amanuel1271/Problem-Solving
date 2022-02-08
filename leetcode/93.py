class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        acc = []
        
        def dfs(string,dot,res):
            if dot == 3:
                if string == '0':
                    acc.append(res + string)
                    return
                elif len(string) != 0 and string[0] != '0' and 1 <= int(string) <= 255:
                    acc.append(res + string)
                    return
                else:
                    return
            elif string == '':
                return
                
            length = len(string)
            dfs(string[1:],dot + 1,res + string[0] + '.')
            for j in range(2,4):
                if length >= j and string[:j][0] != '0' and 1 <= int(string[:j]) <= 255:
                    dfs(string[j:],dot + 1,res + string[:j] + '.')
            
        dfs(s,0,'')
        return acc
