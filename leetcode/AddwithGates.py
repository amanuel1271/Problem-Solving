class Solution {
public:
    int increment(int i){
        unsigned int mask = 1;
        while (i & mask){
            i &= ~mask;
            mask <<= 1;
        }
        
        i |= mask;
        return i;
    }
    
    int getSum(int a, int b) {
        int BITSIZE = 32;
        
        int sum = 0;
        bool carry = 0;
        bool res;
        bool a_pos;
        bool b_pos;
        
        
        for (int i = 0; i < BITSIZE; i = increment(i)){
            a_pos = (a & (1 << i)) >> i;
            b_pos = (b & (1 << i)) >> i;
            res = a_pos ^ b_pos ^ carry;
            sum = sum | (res << i);
            carry = (a_pos & b_pos) | ((a_pos | b_pos) & carry);     
        }
        
        return sum;
        
    }
};
