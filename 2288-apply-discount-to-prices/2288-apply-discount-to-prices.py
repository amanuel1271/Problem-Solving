class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        
        split_s= sentence.split()
        
        for i,word in enumerate(split_s):
            if word[0] == '$' and word[1:].isdigit() and word[1:] != '':
                num = int(word[1:])
                split_s[i] = '$' + str(format(num - (num * discount/100),'.2f'))
        
        return ' '.join(split_s)
                    
                
            
        