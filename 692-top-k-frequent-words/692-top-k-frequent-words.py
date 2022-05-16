class Solution: 
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cntdic = {}
        reverse = {}
        for word in words:
            if word in cntdic:
                cntdic[word] += 1
            else:
                cntdic[word] = 1
                
        for word in cntdic:
            if cntdic[word] in reverse:
                reverse[cntdic[word]].append(word)
            else:
                 reverse[cntdic[word]] = [word]
        
        myheap = []
        
        for count in reverse:
            myheap.append((count,reverse[count]))
            
        heapify(myheap)
        ans  = nlargest(k,myheap)

        
        def GorEq(str1,str2):
            l1,l2 = len(str1),len(str2)
            ilen = min(l1,l2)
            
            for i in range(ilen):
                if str1[i] != str2[i]:
                    return str1[i] > str2[i]
                
            return True if l1 >= l2 else False
        
        def sortlist(wordlist):
            for i in range(len(wordlist)-1,-1,-1):
                for j in range(i):
                    if GorEq(wordlist[j],wordlist[j+1]):
                        wordlist[j],wordlist[j+1] = wordlist[j+1],wordlist[j]
            
                        
            return wordlist
        
        j = 0
        res = []
        broke = False


        
        for cnt,lst in ans:
            for word in sortlist(lst):
                res.append(word)
                j += 1
                if j == k:
                    return res
                
        return res
        
            
            
            
            
            
            
            
            
        