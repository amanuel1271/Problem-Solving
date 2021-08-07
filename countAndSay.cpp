class Solution {
public:
    string countAndSay(int n) {
        if (n == 1)  return string("1");
           
        string prev = countAndSay(n - 1);
        string returnstr = string("");
 
        int i = 0;
        
        while (i < prev.size()){
            char digit = prev[i];
            int count = 1;
            i++;
            
            while (i < prev.size() && prev[i] == digit){
                count++; i++;
            }
            
            returnstr += to_string(count) + digit;
        }
        return returnstr;
        
    }
};
