class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        size = len(arr)
        def find_index():
            diff_index ={}
            for j in range(size): # I dont care if it is overwritten
                diff_index[abs(arr[j]-x)] = j
            
            return diff_index[min(diff_index)]
        
        if size == 1:
            return arr
        
        ptr = find_index()
        if ptr-1 >= 0:
            left,right = ptr-1,ptr
        else:
            left,right = ptr,ptr + 1
        
        
        ans = []
        ans_size = 0
        visited = set()
        
        while ans_size < k:
            if (abs(arr[right]-x) < abs(arr[left]-x) and right not in visited) or left in visited:
                ans.append(arr[right])
                visited.add(right)
                if right != size - 1:
                    right += 1
                ans_size += 1
            else:
                ans.append(arr[left])
                visited.add(left)
                if left != 0:
                    left -= 1
                ans_size += 1
                
        return sorted(ans)
                

            