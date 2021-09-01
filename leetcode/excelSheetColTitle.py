class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num_to_alpha = {}
        NUM_OF_ALPHA = 26
        
        for j in range(NUM_OF_ALPHA):
            num_to_alpha[j] = chr(j + ord('A'))
            
        final_str = ''
            
        while columnNumber:
            final_str = num_to_alpha[(columnNumber - 1) % (NUM_OF_ALPHA)] + final_str
            columnNumber = (columnNumber - 1) // NUM_OF_ALPHA
            
        return final_str
