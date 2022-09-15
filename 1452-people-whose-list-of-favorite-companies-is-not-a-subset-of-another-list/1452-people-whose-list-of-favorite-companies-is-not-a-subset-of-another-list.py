class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        to_set,ans = [],[]
        for i in range(len(favoriteCompanies)):
            to_set.append(set(favoriteCompanies[i]))
            
        for i,s1 in enumerate(to_set):
            set_size = len(s1)
            if any(i != j and (set_size <= len(s2) and len(s1.intersection(s2)) == set_size) for j,s2 in enumerate(to_set)):
                continue
                
            ans.append(i)
                
        return ans
                
            
        