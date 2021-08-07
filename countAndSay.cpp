class Solution {
public:
    string countAndSay(int n) {
        if (n == 1)
            return string("1");
        
                
        string prev = countAndSay(n - 1);
        
        int i = 0;
        string returnstr = string("");
        int len_ = prev.size();
        
        while (i < len_){
            char digit = prev[i];
            int count = 1;
            i++;
            
            while (i < len_ && prev[i] == digit){
                count++;
                i++;
            }
            
            returnstr += to_string(count) + digit;
            
        }
        
        return returnstr;
        
    }
};
