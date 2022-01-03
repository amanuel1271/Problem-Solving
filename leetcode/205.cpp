class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int len_s = s.size(); 
        int len_t = t.size();
        
        if (len_s != len_t)
            return false;
            
        map<char,char> map_;
        for (int i = 0; i < len_s; ++i){
            auto it = map_.find(s[i]);
            if (it != map_.end()){
                if (it->second != t[i])
                    return false;
            }
            else{
                for (auto it = map_.begin(); it != map_.end(); ++it)
                    if (t[i] == it->second){
                        return false;
                    }
                map_.insert(pair<char,char>(s[i],t[i]));   
            }
        
        }
        
        return true;
    }
};
