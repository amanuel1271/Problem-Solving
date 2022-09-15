class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        index_to_set,ans = [],[]
        for i in range(len(favoriteCompanies)):
            index_to_set.append(set(favoriteCompanies[i]))
            
        for i in range(len(favoriteCompanies)):
            set_size = len(index_to_set[i])
            is_subset = False
            for j in range(len(favoriteCompanies)):
                if i == j:
                    continue
                if set_size <= len(index_to_set[j]) and set_size == len(index_to_set[i].intersection(index_to_set[j])):
                    is_subset = True
                    break
            if not is_subset:
                ans.append(i)
                
        return ans
                
            
        