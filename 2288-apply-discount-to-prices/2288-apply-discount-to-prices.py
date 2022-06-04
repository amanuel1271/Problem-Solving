class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        print(sentence.split())
        #rint(format(10,'.2f'))
        
        split_s= sentence.split()
        
        for i,word in enumerate(split_s):
            if word[0] == '$':
                digit = ''
                all_digits = True
                for dig in word[1:]:
                    if dig.isdigit():
                        digit += dig
                    else:
                        all_digits = False
                        break
                        
                if all_digits and digit != '':
                    num = int(digit)
                    split_s[i] = '$' + str(format(num - (num * discount/100),'.2f'))
        
        return ' '.join(split_s)
                    
                
            
        