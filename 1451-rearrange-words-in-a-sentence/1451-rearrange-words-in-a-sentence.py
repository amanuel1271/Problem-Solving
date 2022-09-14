class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split(' ')
        words[0] = words[0][0].lower() + words[0][1:]
        minheap = []
        
        for i in range(len(words)):
            heapq.heappush(minheap,(len(words[i]),i,words[i]))
            
        reconstructed = []
        while minheap:
            reconstructed.append(heapq.heappop(minheap)[2])
        reconstructed[0] = reconstructed[0][0].upper() + reconstructed[0][1:]
        return ' '.join(reconstructed)
            
            
        
        